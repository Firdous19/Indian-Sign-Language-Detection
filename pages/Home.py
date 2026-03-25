# import streamlit as st
# from utils import render_header, init_session_state

# st.set_page_config(page_title="Gestura - Home", page_icon="🏠", layout="wide", initial_sidebar_state="collapsed")
# init_session_state() # Ensure state exists even if user refreshes here
# render_header()      # Show Navbar

# # --- PAGE CONTENT ---
# head_color = "#1e293b" if st.session_state.theme == "Light" else "#f8fafc"

# st.markdown(f"""
# <div style="text-align:center; padding: 40px 0;">
#     <h1 style="font-size: 4rem; margin-bottom: 20px; color: {head_color}; letter-spacing: -2px;">
#         Voice for the Voiceless
#     </h1>
#     <p style="font-size: 1.3rem; opacity: 0.7; max-width: 600px; margin: 0 auto; line-height: 1.6;">
#         Gestura bridges the gap between sign language and speech using advanced Computer Vision.
#     </p>
# </div>
# """, unsafe_allow_html=True)

# c1, c2, c3 = st.columns([1, 1, 1])
# with c2:
#     if st.button("Start Translating 🚀", type="primary", use_container_width=True):
#         st.switch_page("pages/Translate.py")



import streamlit as st
from utils import render_header, init_session_state, get_theme_css

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Gestura | Home", 
    page_icon="🏠", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

init_session_state()
render_header()

# --- DYNAMIC THEME SELECTOR ---
is_dark = st.session_state.theme == "Dark"
bg_color = "#020617" if is_dark else "#f8fafc"
text_color = "#f8fafc" if is_dark else "#1e293b"
subtext_color = "#94a3b8" if is_dark else "#64748b"
accent_color = "#38bdf8" # Cyan
accent_2 = "#818cf8"    # Indigo
card_bg = "rgba(15, 23, 42, 0.6)" if is_dark else "rgba(255, 255, 255, 0.7)"


# --- CUSTOM CSS ---
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');

    .main-font {{ font-family: 'Plus Jakarta Sans', sans-serif; }}

    /* Pulse Animation for CTA */
    @keyframes pulse {{
        0% {{ box-shadow: 0 0 0 0 rgba(56, 189, 248, 0.4); }}
        70% {{ box-shadow: 0 0 0 15px rgba(56, 189, 248, 0); }}
        100% {{ box-shadow: 0 0 0 0 rgba(56, 189, 248, 0); }}
    }}

    .hero-container {{
        text-align: center;
        padding: 60px 0 20px 0;
        max-width: 900px;
        margin: 0 auto;
    }}

    .headline {{
        font-size: 6rem;
        font-weight: 800;
        line-height: 1.1;
        background: linear-gradient(to right, {accent_color}, {accent_2});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 20px;
    }}

    .sub-headline {{
        font-size: 1.4rem;
        color: {subtext_color};
        margin-bottom: 40px;
        line-height: 1.5;
    }}

    /* Mock-up Interface */
    .preview-box {{
        background: {card_bg};
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 24px;
        padding: 20px;
        backdrop-filter: blur(12px);
        margin: 40px auto;
        max-width: 800px;
        position: relative;
        overflow: hidden;
    }}

    .video-mock {{
        width: 100%;
        height: 400px;
        background: #111;
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
    }}

    .skeleton-overlay {{
        position: absolute;
        width: 200px;
        height: 250px;
        border: 2px dashed {accent_color};
        border-radius: 50% 50% 30% 30%;
        opacity: 0.5;
    }}

    .output-label {{
        background: {accent_color};
        color: #000;
        padding: 8px 20px;
        border-radius: 8px;
        font-weight: 700;
        margin-top: 15px;
        display: inline-block;
        font-size: 1.2rem;
    }}

    /* Stats Bar */
    .stats-bar {{
        display: flex;
        justify-content: space-around;
        padding: 40px 0;
        border-top: 1px solid rgba(128,128,128,0.1);
        border-bottom: 1px solid rgba(128,128,128,0.1);
        margin: 40px 0;
    }}

    .stat-item {{ text-align: center; }}
    .stat-val {{ font-size: 1.5rem; font-weight: 800; color: {text_color}; }}
    .stat-lab {{ font-size: 0.8rem; text-transform: uppercase; color: {subtext_color}; letter-spacing: 1px; }}
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown(f"""
<div class="hero-container">
    <h1 class="headline">Giving a Voice to Every Gesture.</h1>
    <p class="sub-headline">
        The most advanced Indian Sign Language interpreter.<br>
        Powered by Deep Learning. Designed for human connection.
    </p>
</div>
""", unsafe_allow_html=True)

# --- CTA BUTTONS ---
c1, c2, c3, c4 = st.columns([1, 0.6, 0.6, 1])
with c2:
    st.markdown('<div class="pulse-btn">', unsafe_allow_html=True)
    if st.button("Launch Camera 🚀", type="primary"):
        st.switch_page("pages/Translate.py")
    st.markdown('</div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="ghost-btn">', unsafe_allow_html=True)
    if st.button("Documentation"):
        st.switch_page("pages/About.py")
    st.markdown('</div>', unsafe_allow_html=True)

# --- LIVE INTERFACE PREVIEW ---
st.markdown(f"""
<div class="preview-box">
    <div style="margin-bottom: 10px; display: flex; gap: 6px;">
        <div style="width: 12px; height: 12px; border-radius: 50%; background: #ff5f56;"></div>
        <div style="width: 12px; height: 12px; border-radius: 50%; background: #ffbd2e;"></div>
        <div style="width: 12px; height: 12px; border-radius: 50%; background: #27c93f;"></div>
    </div>
    <div class="video-mock">
        <div class="skeleton-overlay"></div>
        <p style="color: white; opacity: 0.3; font-size: 0.8rem;">[ CAMERA FEED SIMULATION ]</p>
    </div>
    <div style="text-align: center;">
        <div class="output-label">NAMASTE | नमस्ते</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- QUICK STATS ---
st.markdown(f"""
<div class="stats-bar">
    <div class="stat-item">
        <div class="stat-val">99%</div>
        <div class="stat-lab">Recognition Accuracy</div>
    </div>
    <div class="stat-item">
        <div class="stat-val">&lt; 30ms</div>
        <div class="stat-lab">Processing Latency</div>
    </div>
    <div class="stat-item">
        <div class="stat-val">Native</div>
        <div class="stat-lab">Indian Voice Synthesis</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- HOW IT WORKS ---
st.markdown(f"<h2 style='text-align:center; color:{text_color}; margin-bottom:40px;'>How it Works</h2>", unsafe_allow_html=True)
s1, s2, s3 = st.columns(3)

with s1:
    st.markdown(f"""
    <div style="text-align:center;">
        <div style="font-size: 2rem;">🔓</div>
        <h4 style="color:{text_color}; margin-top:10px;">1. Access</h4>
        <p style="color:{subtext_color}; font-size:0.9rem;">Allow camera access in your browser.</p>
    </div>
    """, unsafe_allow_html=True)

with s2:
    st.markdown(f"""
    <div style="text-align:center;">
        <div style="font-size: 2rem;">✋</div>
        <h4 style="color:{text_color}; margin-top:10px;">2. Sign</h4>
        <p style="color:{subtext_color}; font-size:0.9rem;">Perform ISL gestures clearly in the frame.</p>
    </div>
    """, unsafe_allow_html=True)

with s3:
    st.markdown(f"""
    <div style="text-align:center;">
        <div style="font-size: 2rem;">🔊</div>
        <h4 style="color:{text_color}; margin-top:10px;">3. Speak</h4>
        <p style="color:{subtext_color}; font-size:0.9rem;">The system speaks your sentence instantly.</p>
    </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown(f"<div style='height: 100px;'></div>", unsafe_allow_html=True)