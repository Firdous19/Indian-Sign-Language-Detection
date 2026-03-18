# import streamlit as st
# import cv2
# from detector import StaticISLDetector

# st.set_page_config(page_title="ISL Detector", layout="wide")

# @st.cache_resource
# def load_detector():
#     return StaticISLDetector(model_path="isl_model.pth", classes_path="classes.npy")

# try:
#     detector = load_detector()
# except Exception as e:
#     st.error("Error loading model! Did you run `python train.py` first?")
#     st.stop()

# st.title("🤟 Indian Sign Language (Static Images)")
# st.markdown("Real-time detection of Alphabets and Numbers using Transformer + MediaPipe.")

# col1, col2 = st.columns([2, 1])

# with col1:
#     frame_placeholder = st.empty()

# with col2:
#     st.markdown("### Translation")
#     prediction_text = st.empty()
#     confidence_bar = st.progress(0)
#     confidence_text = st.empty()
    
#     st.markdown("---")
#     # Using a toggle is much more stable than buttons for camera loops in Streamlit
#     run_camera = st.toggle("Power Camera On/Off", value=False)

# if run_camera:
#     cap = cv2.VideoCapture(0)
    
#     while run_camera:
#         ret, frame = cap.read()
#         if not ret:
#             st.error("Failed to read from camera")
#             break
            
#         frame = cv2.flip(frame, 1)
#         prediction, confidence, processed_frame = detector.predict_frame(frame)
        
#         # FIX 1: Changed use_column_width to use_container_width
#         frame_placeholder.image(cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB), channels="RGB", use_container_width=True)
        
#         if prediction == "No Hand Detected":
#             prediction_text.info(prediction)
#             confidence_bar.progress(0)
#             confidence_text.text("Confidence: 0%")
#         else:
#             prediction_text.markdown(f"<h1 style='text-align: center; color: green;'>{prediction}</h1>", unsafe_allow_html=True)
#             confidence_bar.progress(float(confidence))
#             confidence_text.text(f"Confidence: {confidence:.2%}")

#     cap.release()
    
# # FIX 2: Safely clear the placeholder when camera is off to prevent MediaFileStorageError
# if not run_camera:
#     frame_placeholder.empty()
#     prediction_text.info("Camera is Offline")
#     confidence_bar.progress(0)
#     confidence_text.text("Confidence: 0%")
    
    
    
import streamlit as st
from utils import init_session_state

st.set_page_config(
    page_title="Gestura", 
    page_icon="🤏", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# Initialize global state (Camera, Theme)
init_session_state()

# Redirect immediately to the Home page
st.switch_page("pages/Home.py")