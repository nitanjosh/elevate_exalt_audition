import streamlit as st
import datetime
from config import REGISTRATION_DEADLINE, PAGE_CONFIG
import base64

st.set_page_config(**PAGE_CONFIG)
registration_open = datetime.datetime.now() < REGISTRATION_DEADLINE

# Function to load and encode image
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Get base64 encoded logos
logo_dark_base64 = get_base64_image("assets/elevate-exalt_dark.png")
logo_light_base64 = get_base64_image("assets/elevate-exalt_light.png")

st.markdown(f"""
    <style>
    /* Hide default Streamlit elements for cleaner look */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    
    /* Container for proper absolute positioning */
    .header-container {{
        position: relative;
        width: 100%;
        min-height: 100px;
    }}
    
    /* Logo positioned in top-right corner (scrolls with content) */
    .logo-corner {{
        position: absolute;
        top: 1rem;
        right: 1rem;
        width: 120px;
        z-index: 999;
    }}
    
    /* Show dark logo in dark mode, light logo in light mode */
    .logo-dark {{
        display: none;
    }}
    
    .logo-light {{
        display: block;
    }}
    
    @media (prefers-color-scheme: dark) {{
        .logo-dark {{
            display: block;
        }}
        
        .logo-light {{
            display: none;
        }}
    }}
    
    /* For Streamlit's theme detection */
    [data-theme="dark"] .logo-dark,
    body[data-theme="dark"] .logo-dark {{
        display: block;
    }}
    
    [data-theme="dark"] .logo-light,
    body[data-theme="dark"] .logo-light {{
        display: none;
    }}
    
    [data-theme="light"] .logo-dark,
    body[data-theme="light"] .logo-dark {{
        display: none;
    }}
    
    [data-theme="light"] .logo-light,
    body[data-theme="light"] .logo-light {{
        display: block;
    }}
    
    /* Hero section styling */
    .hero-container {{
        text-align: center;
        padding: 3rem 0 2rem 0;
    }}
    
    /* Enhanced hero title with modern gradient */
    .hero-title {{
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
        line-height: 1.2;
    }}
    
    [data-theme="dark"] .hero-title {{
        background: linear-gradient(135deg, #8b9eff 0%, #a78bfa 50%, #f5b8ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }}
    
    /* Subtitle enhancement */
    .hero-subtitle {{
        font-size: 1.3rem;
        color: #6c757d;
        font-weight: 400;
        margin-bottom: 1.5rem;
        letter-spacing: 0.02em;
    }}
    
    [data-theme="dark"] .hero-subtitle {{
        color: #adb5bd;
    }}
    
    /* Animated status indicator */
    .status-indicator {{
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: #d4edda;
        color: #155724;
        padding: 0.5rem 1.2rem;
        border-radius: 25px;
        font-size: 0.9rem;
        font-weight: 600;
        margin: 1rem 0 2rem 0;
        box-shadow: 0 2px 8px rgba(21, 87, 36, 0.15);
    }}
    
    .status-indicator-closed {{
        background: #f8d7da;
        color: #721c24;
        box-shadow: 0 2px 8px rgba(114, 28, 36, 0.15);
    }}
    
    /* Pulsing dot animation */
    .status-dot {{
        width: 8px;
        height: 8px;
        background: #28a745;
        border-radius: 50%;
        animation: pulse 2s ease-in-out infinite;
        box-shadow: 0 0 0 0 rgba(40, 167, 69, 0.7);
    }}
    
    .status-dot-closed {{
        background: #dc3545;
        animation: none;
    }}
    
    @keyframes pulse {{
        0%, 100% {{
            box-shadow: 0 0 0 0 rgba(40, 167, 69, 0.7);
        }}
        50% {{
            box-shadow: 0 0 0 6px rgba(40, 167, 69, 0);
        }}
    }}
    
    /* Divider */
    .divider {{
        height: 1px;
        background: linear-gradient(90deg, transparent, #e9ecef, transparent);
        margin: 2rem 0;
    }}
    
    /* Song card styling */
    .song-card {{
        background: #f8f9fa;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        border: 1px solid #e9ecef;
        transition: transform 0.2s, box-shadow 0.2s;
    }}
    
    .song-card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }}
    
    [data-theme="dark"] .song-card {{
        background: #1e1e1e;
        border: 1px solid #333;
    }}
    
    .song-title {{
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        color: #495057;
    }}
    
    [data-theme="dark"] .song-title {{
        color: #e9ecef;
    }}
    
    .song-artist {{
        font-size: 0.9rem;
        color: #6c757d;
        margin-bottom: 1rem;
    }}
    </style>
""", unsafe_allow_html=True)

# Header with logo
st.markdown(f"""
    <div class="header-container">
        <img src="data:image/png;base64,{logo_light_base64}" class="logo-corner logo-light" alt="Elevate Exalt Logo">
        <img src="data:image/png;base64,{logo_dark_base64}" class="logo-corner logo-dark" alt="Elevate Exalt Logo">
    </div>
""", unsafe_allow_html=True)

# Hero Section with animated status indicator
if registration_open:
    st.markdown("""
        <div class="hero-container">
            <div class="hero-title">ELEVATE EXALT FELIZ</div>
            <div class="hero-subtitle">Audition Application Portal</div>
            <div class="status-indicator">
                <span class="status-dot"></span>
                Registration Open
            </div>
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <div class="hero-container">
            <div class="hero-title">ELEVATE EXALT FELIZ</div>
            <div class="hero-subtitle">Audition Application Portal</div>
            <div class="status-indicator status-indicator-closed">
                <span class="status-dot status-dot-closed"></span>
                Registration Closed
            </div>
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

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Songs for Audition Section
st.markdown("### Songs to Prepare")
st.markdown("""
<p style="color: #6c757d; font-size: 0.9rem; margin-bottom: 1.5rem;">
    Study these songs before your audition. Click the buttons below to watch and learn.
</p>
""", unsafe_allow_html=True)

song_col1, song_col2 = st.columns(2)

with song_col1:
    st.markdown("""
        <div class="song-card">
            <div class="song-title">By Your Love</div>
            <div class="song-artist">CCF Exalt</div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("▶️ Watch on YouTube", "https://www.youtube.com/watch?v=KHyrPzINgyE", use_container_width=True)

with song_col2:
    st.markdown("""
        <div class="song-card">
            <div class="song-title">What A Beautiful Name</div>
            <div class="song-artist">Hillsong Worship</div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("▶️ Watch on YouTube", "https://www.youtube.com/watch?v=nQWFzMvCfLE", use_container_width=True)

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