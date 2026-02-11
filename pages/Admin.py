import streamlit as st
from tools.add_data import get_all_applicants
from tools.db import verify_admin
from config import PAGE_CONFIG

# Page config
st.set_page_config(**PAGE_CONFIG)

# Custom CSS for minimalistic design
st.markdown("""
    <style>
    /* Reduce whitespace */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 1rem;
    }
    
    /* Clean header */
    h1 {
        font-weight: 600;
        margin-bottom: 1.5rem;
    }
    
    /* Subtle cards */
    .stAlert {
        padding: 0.75rem 1rem;
    }
    
    /* Clean buttons */
    .stButton button {
        border-radius: 6px;
    }
    
    /* Compact dataframe */
    .dataframe {
        font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Login screen
if not st.session_state.authenticated:
   
    st.markdown("""
    <div style='display: flex; justify-content: center;'>
        <h1>Admin Login</h1>
    </div>
    """, unsafe_allow_html=True)    
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        username = st.text_input("Username", placeholder="Enter username")
        password = st.text_input("Password", type="password", placeholder="Enter password")
        
        if st.button("Login", type="primary", use_container_width=True):
            if verify_admin(username, password):
                st.session_state.authenticated = True
                st.session_state.admin_username = username
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid credentials")

# Admin dashboard
else:
    # Top bar with theme toggle
    col1, col2, col3 = st.columns([5, 0.5, 1])
    with col1:
        st.markdown("<h1>Exalt Auditionee Applications</h1>", unsafe_allow_html=True)
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🌙" if st.session_state.theme == 'light' else "☀️", key="theme_toggle_admin"):
            st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'
            st.rerun()
    with col3:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Logout", use_container_width=True):
            # Clear authentication
            st.session_state.authenticated = False
            if 'admin_username' in st.session_state:
                del st.session_state.admin_username
            st.rerun()
    
    st.divider()
    
    # Fetch data
    df = get_all_applicants()
    
    if not df.empty:
        # Add display number and remove id column
        display_df = df.copy()
        
        # Add sequential number column at the start
        display_df.insert(0, 'No.', range(1, len(display_df) + 1))
        
        # Remove id column if it exists
        if 'id' in display_df.columns:
            display_df = display_df.drop(columns=['id'])
        
        # Stats row
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Applications", len(df))
        with col2:
            st.metric("Latest Entry", df.iloc[-1]['name'] if 'name' in df.columns else "N/A")
        with col3:
            csv = display_df.to_csv(index=False)
            st.download_button(
                "⬇ Download CSV",
                data=csv,
                file_name="audition_applicants.csv",
                mime="text/csv",
                use_container_width=True
            )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Data table
        st.dataframe(
            display_df,
            use_container_width=True,
            height=500,
            hide_index=True
        )
    else:
        st.info("No applications yet")