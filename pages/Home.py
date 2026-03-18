import streamlit as st
from utils import render_header, init_session_state

st.set_page_config(page_title="Gestura - Home", page_icon="🏠", layout="wide", initial_sidebar_state="collapsed")
init_session_state() # Ensure state exists even if user refreshes here
render_header()      # Show Navbar

# --- PAGE CONTENT ---
head_color = "#1e293b" if st.session_state.theme == "Light" else "#f8fafc"

st.markdown(f"""
<div style="text-align:center; padding: 40px 0;">
    <h1 style="font-size: 4rem; margin-bottom: 20px; color: {head_color}; letter-spacing: -2px;">
        Voice for the Voiceless
    </h1>
    <p style="font-size: 1.3rem; opacity: 0.7; max-width: 600px; margin: 0 auto; line-height: 1.6;">
        Gestura bridges the gap between sign language and speech using advanced Computer Vision.
    </p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns([1, 1, 1])
with c2:
    if st.button("Start Translating 🚀", type="primary", use_container_width=True):
        st.switch_page("pages/Translate.py")