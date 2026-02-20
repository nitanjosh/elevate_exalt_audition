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
    
    /* Remove top padding from main container */
    .main .block-container {{
        padding-top: 2rem;
        max-width: 100%;
    }}
    
    /* Container for header with both logo and status - Flexbox for alignment */
    .header-container {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        padding: 1rem 1rem 1.5rem 1rem;
        margin-bottom: 0.5rem;
    }}
    
    /* Status indicator in top-left corner */
    .status-corner {{
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
    }}
    
    .status-corner-open {{
        background: #d4edda;
        color: #155724;
        border: 1px solid #c3e6cb;
    }}
    
    .status-corner-closed {{
        background: #f8d7da;
        color: #721c24;
        border: 1px solid #f5c6cb;
    }}
    
    [data-theme="dark"] .status-corner-open {{
        background: #1e4620;
        color: #a3cfbb;
        border: 1px solid #2d5a2e;
    }}
    
    [data-theme="dark"] .status-corner-closed {{
        background: #4a1f1f;
        color: #f5b8b8;
        border: 1px solid #5a2828;
    }}
    
    .status-dot {{
        width: 8px;
        height: 8px;
        background: #28a745;
        border-radius: 50%;
        animation: pulse 2s ease-in-out infinite;
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
    
    /* Logo positioned in top-right corner */
    .logo-corner {{
        width: 120px;
        height: auto;
        flex-shrink: 0;
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
        padding: 1rem 0 2rem 0;
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
    
    /* Divider */
    .divider {{
        height: 1px;
        background: linear-gradient(90deg, transparent, #e9ecef, transparent);
        margin: 2rem 0;
    }}
    
    /* Enhanced song card with thumbnail */
    .song-card-enhanced {{
        background: #ffffff;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        border: 1px solid #e9ecef;
        margin-bottom: 1rem;
    }}
    
    .song-card-enhanced:hover {{
        transform: translateY(-4px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    }}
    
    [data-theme="dark"] .song-card-enhanced {{
        background: #1e1e1e;
        border: 1px solid #333;
    }}
    
    .song-thumbnail {{
        position: relative;
        width: 100%;
        height: 180px;
        background-size: cover;
        background-position: center;
        background-color: #f0f0f0;
    }}
    
    .play-overlay {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        background: rgba(0,0,0,0.3);
        transition: all 0.3s ease;
        text-decoration: none;
    }}
    
    .play-overlay:hover {{
        background: rgba(0,0,0,0.5);
    }}
    
    .play-circle {{
        width: 60px;
        height: 60px;
        background: rgba(255,255,255,0.95);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        color: #667eea;
        transition: all 0.3s ease;
        padding-left: 4px;
    }}
    
    .play-overlay:hover .play-circle {{
        transform: scale(1.1);
        background: #ffffff;
    }}
    
    .song-details {{
        padding: 1.25rem;
    }}
    
    .song-details .song-title {{
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 0.3rem;
        color: #2d3748;
    }}
    
    [data-theme="dark"] .song-details .song-title {{
        color: #e9ecef;
    }}
    
    .song-details .song-artist {{
        font-size: 0.9rem;
        color: #6c757d;
        margin-bottom: 0;
    }}
    
    [data-theme="dark"] .song-details .song-artist {{
        color: #adb5bd;
    }}

    /* Bigger CTA button */
    div[data-testid="stButton"] button {{
        height: 70px;
        font-size: 1.2rem;
        font-weight: 700;
        letter-spacing: 0.03em;
    }}
    
    /* Responsive adjustments */
    @media (max-width: 768px) {{
        .hero-title {{
            font-size: 2.5rem;
        }}
        
        .hero-subtitle {{
            font-size: 1.1rem;
        }}
        
        .logo-corner {{
            width: 90px;
        }}
        
        .status-corner {{
            font-size: 0.75rem;
            padding: 0.4rem 0.8rem;
        }}
        
        .header-container {{
            padding: 0.75rem 0.5rem 1rem 0.5rem;
        }}
        
        /* Add spacing between stacked song cards on mobile */
        .song-card-enhanced {{
            margin-bottom: 1.5rem;
        }}
        
        .song-thumbnail {{
            height: 160px;
        }}

        div[data-testid="stButton"] button {{
            height: 60px;
            font-size: 1.05rem;
        }}
    }}
    
    @media (max-width: 480px) {{
        .hero-title {{
            font-size: 2rem;
        }}
        
        .hero-subtitle {{
            font-size: 1rem;
        }}
        
        .logo-corner {{
            width: 80px;
        }}
        
        .status-corner {{
            font-size: 0.7rem;
            padding: 0.35rem 0.7rem;
        }}
        
        /* More spacing between cards on smaller mobile screens */
        .song-card-enhanced {{
            margin-bottom: 2rem;
        }}
    }}
    </style>
""", unsafe_allow_html=True)

# Header with logo and status indicator (aligned with flexbox)
if registration_open:
    st.markdown(f"""
        <div class="header-container">
            <div class="status-corner status-corner-open">
                <span class="status-dot"></span>
                <span>Open</span>
            </div>
            <img src="data:image/png;base64,{logo_light_base64}" class="logo-corner logo-light" alt="Elevate Exalt Logo">
            <img src="data:image/png;base64,{logo_dark_base64}" class="logo-corner logo-dark" alt="Elevate Exalt Logo">
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"""
        <div class="header-container">
            <div class="status-corner status-corner-closed">
                <span class="status-dot status-dot-closed"></span>
                <span>Closed</span>
            </div>
            <img src="data:image/png;base64,{logo_light_base64}" class="logo-corner logo-light" alt="Elevate Exalt Logo">
            <img src="data:image/png;base64,{logo_dark_base64}" class="logo-corner logo-dark" alt="Elevate Exalt Logo">
        </div>
    """, unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div class="hero-container">
        <div class="hero-title">ELEVATE EXALT FELIZ</div>
        <div class="hero-subtitle">Audition Application Portal</div>
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

# Songs for Audition Section with Embedded Thumbnails
st.markdown("### Songs to Prepare")
st.markdown("""
<p style="color: #6c757d; font-size: 0.9rem; margin-bottom: 1.5rem;">
    Study these songs before your audition. Click on the thumbnail to watch on YouTube.
</p>
""", unsafe_allow_html=True)

song_col1, song_col2 = st.columns(2)

with song_col1:
    st.markdown("""
        <div class="song-card-enhanced">
            <div class="song-thumbnail" style="background-image: url('https://img.youtube.com/vi/KHyrPzINgyE/maxresdefault.jpg');">
                <a href="https://www.youtube.com/watch?v=KHyrPzINgyE" target="_blank" class="play-overlay">
                    <div class="play-circle">▶</div>
                </a>
            </div>
            <div class="song-details">
                <div class="song-title">By Your Love</div>
                <div class="song-artist">CCF Exalt</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with song_col2:
    st.markdown("""
        <div class="song-card-enhanced">
            <div class="song-thumbnail" style="background-image: url('https://img.youtube.com/vi/nQWFzMvCfLE/maxresdefault.jpg');">
                <a href="https://www.youtube.com/watch?v=nQWFzMvCfLE" target="_blank" class="play-overlay">
                    <div class="play-circle">▶</div>
                </a>
            </div>
            <div class="song-details">
                <div class="song-title">What A Beautiful Name</div>
                <div class="song-artist">Hillsong Worship</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

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