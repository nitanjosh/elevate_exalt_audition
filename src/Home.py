import streamlit as st
import datetime
from config import REGISTRATION_DEADLINE
from theme_utils import apply_theme, theme_toggle_button

st.set_page_config(
    page_title="Exalt Audition System",
    page_icon="🎵",
    layout="centered"
)

# Apply theme
apply_theme()

# Theme toggle
theme_toggle_button()

# Check registration status
registration_open = datetime.datetime.now() < REGISTRATION_DEADLINE

st.markdown("""
    <style>
    /* Hide default Streamlit elements for cleaner look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Hero section styling */
    .hero-container {
        text-align: center;
        padding: 3rem 0 2rem 0;
    }
    
    .hero-title {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        color: #6c757d;
        font-weight: 300;
        margin-bottom: 2rem;
    }
    
    /* Status indicator */
    .status-badge-open {
        display: inline-block;
        background: #d4edda;
        color: #155724;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
        margin: 1rem 0 2rem 0;
    }
    
    .status-badge-closed {
        display: inline-block;
        background: #f8d7da;
        color: #721c24;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
        margin: 1rem 0 2rem 0;
    }
    
    /* Divider */
    .divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #e9ecef, transparent);
        margin: 2rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Hero Section with dynamic status
if registration_open:
    st.markdown("""
        <div class="hero-container">
            <div class="hero-title">Elevate Exalt Feliz</div>
            <div class="hero-subtitle">Audition Management System</div>
            <div class="status-badge-open">Registration Open</div>
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <div class="hero-container">
            <div class="hero-title">Elevate Exalt Feliz</div>
            <div class="hero-subtitle">Audition Management System</div>
            <div class="status-badge-closed">Registration Closed</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Important Dates Section
st.markdown("### Important Dates")

date_col1, date_col2 = st.columns(2)

with date_col1:
    st.markdown("""
        **Audition Dates**
        - February 21, 2026 at 5:00 PM
        - March 7, 2026 at 5:00 PM
    """)

with date_col2:
    st.markdown("""
        **Interview Dates**
        - February 28, 2026 at 5:00 PM
        - March 14, 2026 at 5:00 PM
    """)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Categories Section
st.markdown("### Audition Categories")

cat_col1, cat_col2 = st.columns(2)

with cat_col1:
    with st.expander("🎹 Band Instruments", expanded=False):
        st.markdown("""
        - Acoustic Guitar
        - Electric Guitar
        - Bass Guitar
        - Drums
        - Keyboard
        """)

with cat_col2:
    with st.expander("🎤 Vocal", expanded=False):
        st.markdown("""
        - Worship Leader (Only if DLeader)
        - Prompter (Support for Worship Leader)
        """)

# Footer with Call to Action
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Dynamic CTA based on registration status
if registration_open:
    st.markdown("""
        <div style="text-align: center; padding: 2rem 0 1rem 0;">
            <p style="color: #6c757d; font-size: 0.9rem; margin-bottom: 1rem;">
                Are you ready to serve the Lord?
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # CTA Button
    col_left, col_center, col_right = st.columns([1, 2, 1])
    with col_center:
        if st.button("🎵 Start Your Application", type="primary", use_container_width=True):
            st.switch_page("pages/Apply.py")
else:
    st.markdown("""
        <div style="text-align: center; padding: 2rem 0 1rem 0;">
            <p style="color: #721c24; font-size: 0.9rem; margin-bottom: 1rem;">
                Registration has closed. Thank you for your interest!
            </p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div style="text-align: center; padding: 1rem 0; color: #adb5bd; font-size: 0.8rem;">
        Questions? Contact <a href="https://www.facebook.com/nitan.jos/" target="_blank" style="color: #adb5bd; text-decoration: underline;">Kuya Nethan</a>
    </div>
""", unsafe_allow_html=True)