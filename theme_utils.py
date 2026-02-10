# theme_utils.py
import streamlit as st

def init_theme():
    """Initialize theme in session state"""
    if 'theme' not in st.session_state:
        st.session_state.theme = 'dark'

def apply_theme():
    """Apply theme-specific CSS"""
    init_theme()
    
    if st.session_state.theme == 'dark':
        st.markdown("""
            <style>
            :root {
                --bg-primary: #0e1117;
                --bg-secondary: #262730;
                --text-primary: #fafafa;
                --text-secondary: #a3a8b8;
                --border-color: #464b5e;
            }
            
            .stApp {
                background-color: var(--bg-primary);
                color: var(--text-primary);
            }
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            :root {
                --bg-primary: #ffffff;
                --bg-secondary: #f8f9fa;
                --text-primary: #212529;
                --text-secondary: #6c757d;
                --border-color: #e9ecef;
            }
            
            .stApp {
                background-color: var(--bg-primary);
                color: var(--text-primary);
            }
            </style>
        """, unsafe_allow_html=True)

def theme_toggle_button():
    """Render theme toggle button"""
    init_theme()
    
    col1, col2 = st.columns([11, 1])
    with col2:
        if st.button("🌙" if st.session_state.theme == 'light' else "☀️", key="theme_toggle"):
            st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'
            st.rerun()