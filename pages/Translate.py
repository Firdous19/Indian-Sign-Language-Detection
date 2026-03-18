import streamlit as st
import cv2
import time
import os
import sys
import pyttsx3
from threading import Thread

# --- PATH RESOLUTION ---
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..')) 
sys.path.append(BACKEND_DIR)

MODEL_PATH = os.path.join(BACKEND_DIR, 'isl_model.pth')
CLASSES_PATH = os.path.join(BACKEND_DIR, 'classes.npy')
TASK_PATH = os.path.join(BACKEND_DIR, 'hand_landmarker.task')

# Assuming you have a utils.py in the same folder or root
try:
    from utils import render_header, init_session_state
except ImportError:
    def render_header(): pass
    def init_session_state(): pass

# --- CONFIG ---
st.set_page_config(page_title="Gestura - Translate", page_icon="📷", layout="wide", initial_sidebar_state="collapsed")
init_session_state()
render_header()

# --- CALLBACKS (MUST BE DEFINED BEFORE UI) ---
def cb_toggle_camera():
    """Logic to handle camera cleanup when toggled off."""
    if not st.session_state.get("camera_active", False):
        if "camera" in st.session_state and st.session_state.camera is not None:
            st.session_state.camera.release()
            st.session_state.camera = None

def cb_space():
    if st.session_state.current_word:
        st.session_state.sentence += st.session_state.current_word + " "
        st.session_state.current_word = ""

def cb_del():
    if st.session_state.current_word:
        st.session_state.current_word = st.session_state.current_word[:-1]
    elif st.session_state.sentence:
        words = st.session_state.sentence.strip().split()
        if words:
            st.session_state.sentence = " ".join(words[:-1]) + (" " if len(words) > 1 else "")

def cb_clear():
    st.session_state.sentence = ""
    st.session_state.current_word = ""

def speak_text(text):
    if not text:
        return
    def _speak():
        try:
            # Note: pyttsx3 can sometimes struggle in threaded web environments
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        except Exception as e: 
            print(f"TTS Error: {e}")
    Thread(target=_speak).start()

# --- INIT DETECTION STATE ---
if "stable_cnt" not in st.session_state:
    st.session_state.stable_cnt = 0
if "last_pred" not in st.session_state:
    st.session_state.last_pred = ""
if "camera" not in st.session_state:
    st.session_state.camera = None
if "current_word" not in st.session_state:
    st.session_state.current_word = ""
if "sentence" not in st.session_state:
    st.session_state.sentence = ""

# --- LOAD MODEL ---
@st.cache_resource
def load_model():
    try:
        from detector import StaticISLDetector
        if os.path.exists(MODEL_PATH): 
            return StaticISLDetector(model_path=MODEL_PATH, classes_path=CLASSES_PATH, task_path=TASK_PATH)
        else:
            st.error(f"Model not found at {MODEL_PATH}.")
    except Exception as e: 
        st.error(f"Error loading model: {e}")
    return None

predictor = load_model()

# --- UI LAYOUT ---
col_cam, col_ui = st.columns([1.8, 1.2], gap="large")

with col_cam:
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    h1, h2 = st.columns([4, 1])
    h1.markdown('<div style="font-size: 1.5rem;font-weight: 600; color: inherit; margin-bottom: 10px" class="section-title">📹 Video Input</div>', unsafe_allow_html=True)
    
    # Callback added here to fix the NameError
    camera_active = h2.toggle("Active", key="camera_active", on_change=cb_toggle_camera)
    
    video_ph = st.empty()
    
    if not camera_active:
        video_ph.markdown('<div style="height:400px; display:flex; align-items:center; justify-content:center; border:2px dashed #475569; border-radius:12px; opacity:0.5;">Camera Paused</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

with col_ui:
    # Word Display
    st.markdown('<div class="card-container border-cyan"><div style="opacity:0.6; font-size:0.8rem; font-weight:700; margin-bottom:10px;">CONSTRUCTING WORD</div>', unsafe_allow_html=True)
    word_ph = st.empty()
    word_ph.markdown(f'<div class="detect-text" style="font-size: 2rem; color: #00ffcc;">{st.session_state.current_word or "..."}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Sentence Display
    st.markdown('<div class="card-container border-indigo"><div style="opacity:0.6; font-size:0.9rem; font-weight:700;">FULL SENTENCE</div>', unsafe_allow_html=True)
    sent_ph = st.empty()
    sent_ph.markdown(f'<div style="font-family:monospace; min-height:80px; font-size: 20px">{st.session_state.sentence or "Waiting..."}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Controls
    c1, c2, c3 = st.columns(3)
    c1.button("␣ Space", use_container_width=True, on_click=cb_space)
    c2.button("⌫ Del", use_container_width=True, on_click=cb_del)
    c3.button("🗑 Clr", use_container_width=True, on_click=cb_clear)

    st.button("🔊 Speak", type="primary", use_container_width=True, on_click=lambda: speak_text(st.session_state.sentence))

# --- DETECTION LOOP ---
if st.session_state.camera_active and predictor:
    if st.session_state.camera is None or not st.session_state.camera.isOpened():
        st.session_state.camera = cv2.VideoCapture(0)
    
    cam = st.session_state.camera
    
    try:
        while st.session_state.camera_active:
            ret, frame = cam.read()
            if not ret:
                st.error("Camera disconnected")
                break
            
            # Predict on raw unmirrored frame
            label, conf, proc = predictor.predict_frame(frame)
            
            # Mirror frame for UI visualization
            proc = cv2.flip(proc, 1)
            
            # Draw UI Overlay on Frame
            h, w, _ = proc.shape
            cv2.rectangle(proc, (0, h-50), (w, h), (0,0,0), -1)
            
            if label != "No Hand Detected" and conf > 0.75:
                cv2.putText(proc, f"Sign: {label} ({conf:.2f})", (20, h-15), 
                            cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255), 1)
                
                if label == st.session_state.last_pred: 
                    st.session_state.stable_cnt += 1
                else: 
                    st.session_state.stable_cnt = 0
                    st.session_state.last_pred = label
                
                # Progress Bar logic
                prog = min(st.session_state.stable_cnt / 10, 1.0)
                cv2.rectangle(proc, (0, h-5), (int(w*prog), h), (0, 255, 0), -1)
                
                # Confirmation Logic
                if st.session_state.stable_cnt == 10:
                    if label == "Space": 
                        cb_space()
                    elif label in ["Del", "Delete"]: 
                        cb_del()
                    elif label not in ["Unknown Sign", "Nothing"]: 
                        st.session_state.current_word += label
                    
                    st.session_state.stable_cnt = 0
                    
                    # Update UI Placeholders
                    word_ph.markdown(f'<div class="detect-text" style="font-size: 2rem; color: #00ffcc;">{st.session_state.current_word or "..."}</div>', unsafe_allow_html=True)
                    sent_ph.markdown(f'<div style="font-family:monospace; min-height:80px; font-size: 20px">{st.session_state.sentence or "Waiting..."}</div>', unsafe_allow_html=True)
            else:
                st.session_state.stable_cnt = 0
                
            # FIX: Convert BGR to RGB and pass directly to st.image. 
            # This removes the 'format' error and the 'MediaFileStorageError'.
            video_ph.image(cv2.cvtColor(proc, cv2.COLOR_BGR2RGB), use_container_width=True)
            
            time.sleep(0.01)
            
    finally:
        # Cleanup logic
        if not st.session_state.camera_active and st.session_state.camera is not None:
            st.session_state.camera.release()
            st.session_state.camera = None
            video_ph.empty()

# Final safety cleanup
if not st.session_state.camera_active and st.session_state.camera is not None:
    st.session_state.camera.release()
    st.session_state.camera = None