import streamlit as st
import cv2
import os
import math


# --- THEME & CSS ---
def get_theme_css(theme):
    if theme == "Dark":
        bg_color, card_bg, text_color, border_color = "#020617", "#0f172a", "#f8fafc", "#1e293b"
        accent1, accent2 = "#38bdf8", "#818cf8"
        toggle_color = "#000C42"
    else:
        bg_color, card_bg, text_color, border_color = "#f8fafc", "#ffffff", "#141b2d", "#e2e8f0"
        accent1, accent2 = "#0284c7", "#4f46e5"
        toggle_color = "#787A7E"

    return f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
        
        .stApp {{ background-color: {bg_color} !important; color: {text_color} !important; font-family: 'Plus Jakarta Sans', sans-serif; }}
        [data-testid="stSidebar"] {{ display: none; }} /* Hide Default Sidebar */
        header {{ visibility: hidden; }}
        
        /* Navbar */
        .nav-container {{
            display: flex; justify-content: space-between; align-items: center;
            padding-bottom: 1rem; border-bottom: 1px solid {border_color}; margin-bottom: 2rem;
        }}
        .logo-text {{
            font-size: 1.8rem; font-weight: 800;
            background: -webkit-linear-gradient(45deg, {accent1}, {accent2});
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }}
        
        /* Cards */
        .card-container {{
            background-color: {card_bg}; border: 1px solid {border_color};
            border-radius: 16px; padding: 1.5rem; margin-bottom: 1rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }}
        .border-cyan {{ border: 1px solid {accent1} !important; }}
        .border-indigo {{ border: 1px solid {accent2} !important; }}
        
        /* Text & Buttons */
        .detect-text {{ font-size: 2rem; font-weight: 700; color: {text_color}; text-align: center; }}
        div.stButton > button {{
            background-color: {card_bg} !important; color: {text_color} !important;
            border: 1px solid {border_color} !important; border-radius: 8px;
        }}
        div.stButton > button:hover {{ border-color: {accent1} !important; color: {accent1} !important; }}
        div.stButton > button[kind="primary"] {{
            background: linear-gradient(90deg, {accent1}, {accent2}) !important;
            color: white !important; border: none !important;
        }}

        div[data-testid="stCheckbox"] label {{
            display: flex;
            align-items: center;
            gap: 10px
        }}
        
        div[data-testid="stCheckbox"] label > div:first-child {{
            transform: scale(1.4);
            background-color: {toggle_color};
        }}
        
        div[data-testid="stCheckbox"] p {{
            font-size: 17px;
            color: {text_color} !important;
            font-weight: 500;
        }}
    </style>
    """

# --- INITIALIZATION ---
def init_session_state():
    if 'theme' not in st.session_state: st.session_state.theme = "Dark"
    if 'camera' not in st.session_state: st.session_state.camera = cv2.VideoCapture(0)
    if 'camera_active' not in st.session_state: st.session_state.camera_active = False
    if 'sentence' not in st.session_state: st.session_state.sentence = ""
    if 'current_word' not in st.session_state: st.session_state.current_word = ""

# --- SHARED NAVBAR ---
def render_header():
    # Inject CSS
    st.markdown(get_theme_css(st.session_state.theme), unsafe_allow_html=True)
    
    # Remove default top padding
    st.markdown("""
        <style>
            [data-testid="stSidebar"] {
                display: none;
            }
            [data-testid="collapsedControl"] {
                display: none;
            }
            .block-container {
                padding-top: 01rem;
                padding-bottom: 0rem;
            }

            div[data-testid="stHorizontalBlock"] {
                justify-content: space-between;
                align-items: center;
            }

            .logo-text {
                font-size: 40px;
                font-weight: 700;
                margin: 0;
            }

            div[data-testid="stButton"] > button {
                padding: 8px 30px;
                border-radius: 8px;
                font-size: 22px;
                font-weight: 500;
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Custom Navbar Layout
    c1, c2, c3 = st.columns([2, 4, 0.5])
    with c1:
        st.markdown('<div class="logo-text">Gestura</div>', unsafe_allow_html=True)
    with c2:
        # Navigation Buttons (Using switch_page for MPA)
        b1, b_dash, b2, b3, _ = st.columns([1, 1.2, 1, 1, 1])
        if b1.button("Home"): st.switch_page("pages/Home.py")
        if b_dash.button("Dashboard"): st.switch_page("pages/Dashboard.py")
        if b2.button("Translate"): st.switch_page("pages/Translate.py")
        if b3.button("About"): st.switch_page("pages/About.py")
    
    with c3:
        # Theme Toggle
        icon = "🌙" if st.session_state.theme == "Light" else "☀️"
        if st.button(icon, key="theme_toggle"):
            st.session_state.theme = "Light" if st.session_state.theme == "Dark" else "Dark"
            st.rerun()
    st.markdown("---")
    