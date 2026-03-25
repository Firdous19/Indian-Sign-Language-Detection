# import streamlit as st
# from utils import render_header, init_session_state

# st.set_page_config(page_title="Gestura - About", page_icon="ℹ️", layout="wide", initial_sidebar_state="collapsed")
# init_session_state()
# render_header()

# st.markdown('<div class="card-container">', unsafe_allow_html=True)
# st.markdown("### 🤖 About Gestura")
# st.markdown("""
# **Gestura** is a real-time accessibility tool designed to translate Indian Sign Language (ISL) into text and speech.

# **How it works:**
# 1.  **Input:** The camera captures hand gestures.
# 2.  **Detection:** MediaPipe extracts hand landmarks.
# 3.  **Classification:** A custom LSTM/CNN model predicts the sign.
# 4.  **Output:** The sign is converted to text and spoken aloud.

# **Tech Stack:** Python, Streamlit, TensorFlow, OpenCV, MediaPipe.
# """)
# st.markdown('</div>', unsafe_allow_html=True)




# import streamlit as st
# from utils import render_header, init_session_state

# # --- INITIALIZATION ---
# init_session_state()

# # --- PAGE CONFIG ---
# st.set_page_config(
#     page_title="Gestura - About",
#     page_icon="ℹ️",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # --- RENDER CUSTOM NAVBAR & CSS ---
# render_header()

# # --- ADDITIONAL CSS FOR GRID & HIGHLIGHTS ---
# st.markdown("""
# <style>
#     .hero-section {
#         text-align: center;
#         padding: 4rem 0 2rem 0;
#     }
#     .feature-card {
#         height: 100%;
#         transition: all 0.3s ease;
#         border: 1px solid rgba(255,255,255,0.1);
#     }
#     .feature-card:hover {
#         transform: translateY(-8px);
#         border-color: #38bdf8;
#         box-shadow: 0 10px 25px -5px rgba(56, 189, 248, 0.2);
#     }
#     /* Updated Gesture Highlight Section */
#     .gesture-highlight {
#         background: #1e293b;
#         border-radius: 24px;
#         padding: 3rem;
#         border: 1px solid rgba(56, 189, 248, 0.3);
#         margin-top: 4rem;
#         color: white;
#     }
#     .step-number {
#         font-weight: 800;
#         font-size: 1.2rem;
#         color: #38bdf8;
#         margin-bottom: 0.5rem;
#     }
#     .badge {
#         display: inline-block;
#         padding: 4px 14px;
#         border-radius: 50px;
#         font-size: 0.75rem;
#         font-weight: 700;
#         text-transform: uppercase;
#         letter-spacing: 1px;
#         background: rgba(56, 189, 248, 0.15);
#         color: #38bdf8;
#         margin-bottom: 12px;
#     }
#     /* Fixed Image Container */
#     .img-container {
#         display: flex;
#         justify-content: center;
#         align-items: center;
#         padding: 10px;
#         background: rgba(255, 255, 255, 0.03);
#         border-radius: 20px;
#         border: 1px solid rgba(255, 255, 255, 0.1);
#     }
#     .instruction-card {
#         background: rgba(255, 255, 255, 0.05);
#         padding: 20px;
#         border-radius: 16px;
#         border-left: 4px solid #38bdf8;
#         margin: 25px 0;
#     }
# </style>
# """, unsafe_allow_html=True)

# # --- HERO SECTION ---
# st.markdown("""
#     <div class="hero-section">
#         <h1 class="logo-text" style="font-size: 4.5rem; margin-bottom: 1rem;">Empowering Silence.</h1>
#         <p style="font-size: 1.25rem; opacity: 0.7; max-width: 750px; margin: 0 auto; line-height: 1.6;">
#             Gestura is a high-performance accessibility suite bridging the gap between 
#             the <b>Indian Sign Language (ISL)</b> community and the world through real-time AI.
#         </p>
#     </div>
# """, unsafe_allow_html=True)

# # --- OUR VISION SECTION ---
# st.write("---")
# col_v1, col_v2 = st.columns([1.2, 1], gap="large")

# with col_v1:
#     st.markdown("""
#         <div class="card-container" style="border-left: 5px solid #818cf8;">
#             <span class="badge" style="background: rgba(129, 140, 248, 0.15); color: #818cf8;">OUR VISION</span>
#             <h2 style="margin-top:0;">Breaking Communication Barriers</h2>
#             <p style="font-size: 1.1rem; opacity: 0.9;">We believe accessibility is a right, not a privilege. Gestura turns a simple webcam into a sophisticated ISL interpreter, allowing for fluid, real-time conversation.</p>
#             <p style="font-size: 1.1rem; opacity: 0.9;">By combining <b>MediaPipe</b> landmarks with <b>TensorFlow</b> intelligence, we've optimized this system for speed and cultural accuracy.</p>
#         </div>
#     """, unsafe_allow_html=True)

# with col_v2:
#     st.markdown('<div class="card-container">', unsafe_allow_html=True)
#     st.markdown("### 🛠️ Core Tech Stack")
#     st.markdown("""
#     * **Vision Engine:** MediaPipe (21-Point Landmark Extraction)
#     * **Deep Learning:** TensorFlow LSTM Architecture
#     * **Voice Synthesis:** gTTS (Optimized Indian Accent)
#     * **Audio Pipeline:** Pygame Mixer (Low-Latency)
#     * **Interface:** Streamlit Modern UI
#     """)
#     st.markdown('</div>', unsafe_allow_html=True)

# # --- CORE FEATURES GRID ---
# st.markdown("<h2 style='text-align: center; margin-top: 4rem; margin-bottom: 2rem;'>System Capabilities</h2>", unsafe_allow_html=True)

# f1, f2, f3 = st.columns(3)

# with f1:
#     st.markdown("""<div class="card-container feature-card">
#         <div class="step-number">01</div>
#         <h4>Real-time ISL Detection</h4>
#         <p style="font-size: 0.9rem; opacity: 0.7;">Tracks 21 hand landmarks with millisecond precision, ensuring zero lag during active signing.</p>
#     </div>""", unsafe_allow_html=True)

# with f2:
#     st.markdown("""<div class="card-container feature-card">
#         <div class="step-number">02</div>
#         <h4>Indian English Voice</h4>
#         <p style="font-size: 0.9rem; opacity: 0.7;">Localized speech synthesis tailored for the Indian context, providing a familiar and natural auditory experience.</p>
#     </div>""", unsafe_allow_html=True)

# with f3:
#     st.markdown("""<div class="card-container feature-card">
#         <div class="step-number">03</div>
#         <h4>Hybrid Logic Processing</h4>
#         <p style="font-size: 0.9rem; opacity: 0.7;">A fusion of ML models and custom heuristic scripts for 100% reliable system command execution.</p>
#     </div>""", unsafe_allow_html=True)

# # --- GESTURAL CONTROL (THE SPACEBAR) ---
# st.markdown('<div class="gesture-highlight">', unsafe_allow_html=True)
# g_col1, g_col2 = st.columns([1.4, 1], gap="large")

# with g_col1:
#     st.markdown(f"""
#         <span class="badge">UNIQUE INNOVATION</span>
#         <h2 style="font-size: 2.8rem; margin-bottom: 1rem; color: white;">The "Space" Command</h2>
#         <p style="font-size: 1.15rem; line-height: 1.7; opacity: 0.9;">
#             To enable true hands-free communication, we introduced the <b>Gestural Spacebar</b>. 
#             This allows signers to construct complete sentences without ever reaching for a physical keyboard.
#         </p>
#         <div class="instruction-card">
#             <b style="color: #38bdf8; font-size: 1.1rem;">The Gesture:</b><br>
#             <span style="font-size: 1.2rem;">Right Open Palm (Fingers Together, Thumb Tucked)</span><br>
#             <p style="margin-top: 8px; font-size: 0.95rem; opacity: 0.8;">Hold this position briefly to insert a space and finalize your previous word.</p>
#         </div>
#     """, unsafe_allow_html=True)

# with g_col2:
#     # We wrap the image in a container to control the size perfectly
#     st.markdown('<div class="img-container">', unsafe_allow_html=True)
#     st.image("space_gesture.png", width=320) # Forced width for balance
#     st.markdown('</div>', unsafe_allow_html=True)
#     st.markdown('<p style="text-align: center; font-size: 0.85rem; opacity: 0.5; margin-top: 10px;">Visual Reference: Space Control Gesture</p>', unsafe_allow_html=True)

# st.markdown('</div>', unsafe_allow_html=True)

# # --- FOOTER ---
# st.markdown("""
#     <div style="text-align: center; margin-top: 6rem; padding: 2rem; opacity: 0.4; font-size: 0.85rem; border-top: 1px solid rgba(255,255,255,0.1);">
#         Gestura Accessibility Suite • Engineered by <b>Bidisha Mukherjee</b> • 2026
#     </div>
# """, unsafe_allow_html=True)



import streamlit as st
import base64
from utils import render_header, init_session_state

# --- INITIALIZATION ---
init_session_state()

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Gestura - About",
    page_icon="ℹ️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- RENDER CUSTOM NAVBAR & CSS ---
render_header()

# --- IMAGE HELPER FUNCTION ---
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception:
        return ""

# Get the base64 string of your gesture image
img_base64 = get_base64_image("space_gesture.png")

# --- ADDITIONAL CSS ---
st.markdown("""
<style>
    .hero-section {
        text-align: center;
        padding: 4rem 0 2rem 0;
    }
    .feature-card {
        height: 100%;
        transition: all 0.3s ease;
        border: 1px solid rgba(255,255,255,0.1);
    }
    .feature-card:hover {
        transform: translateY(-8px);
        border-color: #38bdf8;
        box-shadow: 0 10px 25px -5px rgba(56, 189, 248, 0.2);
    }
    .gesture-highlight {
        border-radius: 24px;
        padding: 4rem 3rem;
    }
    .badge {
        display: inline-block;
        padding: 4px 14px;
        border-radius: 50px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        background: rgba(56, 189, 248, 0.15);
        color: #38bdf8;
        margin-bottom: 12px;
        font-size: 30px
    }
    .img-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2rem;
        height: 100%;
    }
    .instruction-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 16px;
        border-left: 4px solid #38bdf8;
        margin: 25px 0;
    }
    .step-number {
        font-weight: 800;
        font-size: 1.2rem;
        color: #38bdf8;
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("""
    <div class="hero-section">
        <h1 class="logo-text" style="font-size: 4.5rem; margin-bottom: 1rem;">Empowering Silence.</h1>
        <p style="font-size: 1.25rem; opacity: 0.7; max-width: 750px; margin: 0 auto; line-height: 1.6;">
            Gestura is a high-performance accessibility suite bridging the gap between 
            the <b>Indian Sign Language (ISL)</b> community and the world through real-time AI.
        </p>
    </div>
""", unsafe_allow_html=True)

# --- OUR VISION SECTION ---
st.write("---")
col_v1, col_v2 = st.columns([1.2, 1], gap="large")

with col_v1:
    st.markdown("""
        <div class="card-container" style="border-left: 5px solid #818cf8;">
            <span class="badge" style="background: rgba(129, 140, 248, 0.15); color: #818cf8;">OUR VISION</span>
            <h2 style="margin-top:0;">Breaking Communication Barriers</h2>
            <p style="font-size: 1.1rem; opacity: 0.9;">We believe accessibility is a right, not a privilege. Gestura turns a simple webcam into a sophisticated ISL interpreter, allowing for fluid, real-time conversation.</p>
            <p style="font-size: 1.1rem; opacity: 0.9;">By combining <b>MediaPipe</b> landmarks with <b>TensorFlow</b> intelligence, we've optimized this system for speed and cultural accuracy.</p>
        </div>
    """, unsafe_allow_html=True)

with col_v2:
    st.markdown("""
        <div class="card-container" style="height: 100%;">
            <h3 style="margin-top: 0;">🛠️ Core Tech Stack</h3>
            <ul style="list-style-type: none; padding-left: 0; line-height: 1.8; opacity: 0.9;">
                <li><b style="color: #4F46E5;">• Vision Engine:</b> MediaPipe (21-Point Landmark Extraction)</li>
                <li><b style="color: #4F46E5;">• Deep Learning:</b> TensorFlow LSTM Architecture</li>
                <li><b style="color: #4F46E5;">• Voice Synthesis:</b> gTTS (Optimized Indian Accent)</li>
                <li><b style="color: #4F46E5;">• Audio Pipeline:</b> Pygame Mixer (Low-Latency)</li>
                <li><b style="color: #4F46E5;">• Interface:</b> Streamlit Modern UI</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# --- CORE FEATURES GRID ---
st.markdown("<h2 style='text-align: center; margin-top: 4rem; margin-bottom: 2rem;'>System Capabilities</h2>", unsafe_allow_html=True)

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("""<div class="card-container feature-card">
        <div class="step-number">01</div>
        <h4>Real-time ISL Detection</h4>
        <p style="font-size: 0.9rem; opacity: 0.7;">Tracks 21 hand landmarks with millisecond precision, ensuring zero lag during active signing.</p>
    </div>""", unsafe_allow_html=True)

with f2:
    st.markdown("""<div class="card-container feature-card">
        <div class="step-number">02</div>
        <h4>Indian English Voice</h4>
        <p style="font-size: 0.9rem; opacity: 0.7;">Localized speech synthesis tailored for the Indian context, providing a natural auditory experience.</p>
    </div>""", unsafe_allow_html=True)

with f3:
    st.markdown("""<div class="card-container feature-card">
        <div class="step-number">03</div>
        <h4>Hybrid Logic Processing</h4>
        <p style="font-size: 0.9rem; opacity: 0.7;">A fusion of ML models and custom heuristic scripts for 100% reliable system command execution.</p>
    </div>""", unsafe_allow_html=True)

# --- GESTURAL CONTROL (THE SPACEBAR) ---
st.markdown('<div class="gesture-highlight">', unsafe_allow_html=True)
g_col1, g_col2 = st.columns([1, 1], gap="large")

with g_col1:
    st.markdown(f"""
        <span class="badge">UNIQUE INNOVATION</span>
        <h2 style="font-size: 2.8rem; margin-bottom: 1rem; color: white;">The "Space" Command</h2>
        <p style="font-size: 1.15rem; line-height: 1.7; opacity: 0.9;">
            To enable true hands-free communication, we introduced the <b>Gestural Spacebar</b>. 
            This allows signers to construct complete sentences without ever reaching for a physical keyboard.
        </p>
        <div class="instruction-card">
            <b style="color: #38bdf8; font-size: 1.1rem;">The Gesture:</b><br>
            <span style="font-size: 1.2rem;">Right Open Palm (Fingers Together, Thumb Tucked)</span><br>
            <p style="margin-top: 8px; font-size: 0.95rem; opacity: 0.8;">Hold this position briefly to insert a space and finalize your previous word.</p>
        </div>
    """, unsafe_allow_html=True)

with g_col2:
    st.markdown(f"""
        <div class="img-container">
            <img src="data:image/png;base64,{img_base64}" style="width: 100%; max-width: 320px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
            <p style="text-align: center; font-size: 0.85rem; opacity: 0.5; margin-top: 15px; color: white;">
                Visual Reference: Space Control Gesture
            </p>
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown(f"""
    <div style="text-align: center; margin-top: 6rem; padding: 2rem; opacity: 0.4; font-size: 0.85rem; border-top: 1px solid rgba(255,255,255,0.1);">
        Gestura Accessibility Suite • Engineered by <b>Firdous</b> • 2026
    </div>
""", unsafe_allow_html=True)