import streamlit as st
from utils import render_header, init_session_state

st.set_page_config(page_title="Gestura - About", page_icon="ℹ️", layout="wide", initial_sidebar_state="collapsed")
init_session_state()
render_header()

st.markdown('<div class="card-container">', unsafe_allow_html=True)
st.markdown("### 🤖 About Gestura")
st.markdown("""
**Gestura** is a real-time accessibility tool designed to translate Indian Sign Language (ISL) into text and speech.

**How it works:**
1.  **Input:** The camera captures hand gestures.
2.  **Detection:** MediaPipe extracts hand landmarks.
3.  **Classification:** A custom LSTM/CNN model predicts the sign.
4.  **Output:** The sign is converted to text and spoken aloud.

**Tech Stack:** Python, Streamlit, TensorFlow, OpenCV, MediaPipe.
""")
st.markdown('</div>', unsafe_allow_html=True)