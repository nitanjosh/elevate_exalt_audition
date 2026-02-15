import streamlit as st
import datetime
from tools.add_data import init_df, add_data
from config import REGISTRATION_DEADLINE, PAGE_CONFIG
import base64

init_df()
st.set_page_config(**PAGE_CONFIG)

# Function to load and encode image
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Get base64 encoded logos
logo_dark_base64 = get_base64_image("assets/elevate-exalt_dark.png")
logo_light_base64 = get_base64_image("assets/elevate-exalt_light.png")

# Custom CSS for minimalistic design
st.markdown(f"""
    <style>
    /* Hide default elements */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    
    /* Logo fixed in top-right corner */
    .logo-corner {{
        position: fixed;
        top: 3rem;
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
    
    /* Form container */
    .form-container {{
        background: #ffffff;
        border: 1px solid #e9ecef;
        border-radius: 12px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }}
    
    /* Section headers */
    .section-header {{
        font-size: 0.85rem;
        font-weight: 600;
        color: #6c757d;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin: 1.5rem 0 0.75rem 0;
        border-bottom: 1px solid #e9ecef;
        padding-bottom: 0.5rem;
    }}
    
    /* Page title */
    .page-title {{
        font-size: 2rem;
        font-weight: 600;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }}
    
    .page-subtitle {{
        font-size: 0.95rem;
        color: #6c757d;
        margin-bottom: 2rem;
    }}
    
    /* Required field indicator */
    .required-note {{
        font-size: 0.85rem;
        color: #6c757d;
        font-style: italic;
        margin-bottom: 1.5rem;
    }}
    
    /* Divider */
    .divider {{
        height: 1px;
        background: linear-gradient(90deg, transparent, #e9ecef, transparent);
        margin: 2rem 0;
    }}
    
    /* Review section styling */
    .review-container {{
        background: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
    }}
    
    .review-title {{
        font-size: 1.3rem;
        font-weight: 600;
        color: #212529;
        margin-bottom: 1rem;
    }}
    
    .info-row {{
        display: flex;
        justify-content: space-between;
        padding: 0.5rem 0;
        border-bottom: 1px solid #dee2e6;
    }}
    
    .info-label {{
        font-weight: 500;
        color: #6c757d;
    }}
    
    .info-value {{
        color: #212529;
        text-align: right;
    }}
    </style>
    
    <!-- Logos in top-right corner (theme-aware) -->
    <img src="data:image/png;base64,{logo_light_base64}" class="logo-corner logo-light" alt="Elevate Exalt Logo">
    <img src="data:image/png;base64,{logo_dark_base64}" class="logo-corner logo-dark" alt="Elevate Exalt Logo">
""", unsafe_allow_html=True)

if datetime.datetime.now() > REGISTRATION_DEADLINE:
    st.markdown('<div class="page-title">Registration Closed</div>', unsafe_allow_html=True)
    st.warning("Sorry! The Registration Process is now closed.")
    st.info("For inquiries, please contact your Dgroup Leader.")
else:
    # Page header
    st.markdown('<div class="page-title">Audition Application</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Elevate Exalt Feliz</div>', unsafe_allow_html=True)

    # Personal Information Section
    st.markdown('<div class="section-header">Personal Information</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    first_name = col1.text_input("First Name *", placeholder="Enter your first name")
    last_name = col1.text_input("Last Name *", placeholder="Enter your last name")
    age = col2.number_input("Age", min_value=0, max_value=100, value=0)
    phone = col2.text_input("Phone Number", placeholder="09XX XXX XXXX")

    st.markdown('<div class="section-header">Contact</div>', unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    email = col3.text_input("Email Address *", placeholder="your.email@example.com")
    dleader = col4.text_input("Dgroup Leader *", placeholder="Leader's name")

    st.markdown('<div class="section-header">Audition Details</div>', unsafe_allow_html=True)
    
    category = st.selectbox(
        "Category", 
        ["Band", "Singer"],
        help="Select your audition category"
    )

    if category == "Band":
        instrument = st.selectbox(
            "Instrument",
            ["Acoustic Guitar", "Electric Guitar", "Bass Guitar", "Drums", "Keyboard"],
            help="Select your primary instrument"
        )
    else:
        instrument = "Vocals"

    st.markdown('<div class="section-header">Schedule</div>', unsafe_allow_html=True)
    
    col5, col6 = st.columns(2)
    
    with col5:
        # Define all possible audition dates
        all_audition_dates = ["February 21, 5:00PM", "March 7, 5:00PM"]
        
        # Filter out past dates
        current_datetime = datetime.datetime.now()
        available_audition_dates = []
        
        for date_str in all_audition_dates:
            # Parse the date string
            if "February 21" in date_str:
                date_obj = datetime.datetime(2026, 2, 21, 17, 0)  # 5:00 PM
            elif "March 7" in date_str:
                date_obj = datetime.datetime(2026, 3, 7, 17, 0)  # 5:00 PM
            
            # Only include if date hasn't passed
            if date_obj > current_datetime:
                available_audition_dates.append(date_str)
        
        # Show dropdown or message
        if available_audition_dates:
            aud_date = st.selectbox(
                "Audition Date", 
                available_audition_dates,
                help="Choose your preferred audition date"
            )
        else:
            st.warning("No upcoming audition dates available.")
            aud_date = None
    
    with col6:
        if aud_date:
            if aud_date == "February 21, 5:00PM":
                interview_date = st.selectbox(
                    "Interview Date", 
                    ["February 28, 5:00PM", "March 14, 5:00PM"],
                    help="Choose your preferred interview date"
                )
            else:
                interview_date = st.selectbox(
                    "Interview Date", 
                    ["March 14, 5:00PM"],
                    help="Available interview date for this audition"
                )
        else:
            interview_date = None

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # Submit button
    col_left, col_center, col_right = st.columns([1, 2, 1])
    with col_center:
        submit_clicked = st.button("Continue to Review", type="primary", use_container_width=True)

    if submit_clicked:
        # Validate required fields
        if not first_name or not last_name or not email or not dleader:
            st.error("Please fill in all required fields (marked with *)!")
        elif not aud_date:
            st.error("No audition dates are currently available. Please contact your Dgroup Leader.")
        else:
            st.session_state.pending_data = {
                "first_name": first_name,
                "last_name": last_name,
                "age": age,
                "phone": phone,
                "email": email,
                "dleader": dleader,
                "category": category,
                "instrument": instrument,
                "aud_date": aud_date,
                "interview_date": interview_date,
            }
            st.session_state.show_confirmation = True
            st.rerun()

# Confirmation dialog
if st.session_state.get("show_confirmation", False):
    data = st.session_state.pending_data
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="review-title">Review Your Application</div>', unsafe_allow_html=True)
    
    # Review information in a clean format
    st.markdown('<div class="review-container">', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="info-row">
        <span class="info-label">Full Name</span>
        <span class="info-value">{data['first_name']} {data['last_name']}</span>
    </div>
    <div class="info-row">
        <span class="info-label">Age</span>
        <span class="info-value">{data['age']}</span>
    </div>
    <div class="info-row">
        <span class="info-label">Email</span>
        <span class="info-value">{data['email']}</span>
    </div>
    <div class="info-row">
        <span class="info-label">Phone</span>
        <span class="info-value">{data['phone']}</span>
    </div>
    <div class="info-row">
        <span class="info-label">Dgroup Leader</span>
        <span class="info-value">{data['dleader']}</span>
    </div>
    <div class="info-row">
        <span class="info-label">Category</span>
        <span class="info-value">{data['category']}</span>
    </div>
    <div class="info-row">
        <span class="info-label">Instrument</span>
        <span class="info-value">{data['instrument']}</span>
    </div>
    <div class="info-row">
        <span class="info-label">Audition Date</span>
        <span class="info-value">{data['aud_date']}</span>
    </div>
    <div class="info-row" style="border-bottom: none;">
        <span class="info-label">Interview Date</span>
        <span class="info-value">{data['interview_date']}</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.warning("Confirm personal details before submitting.")
    
    col_yes, col_no, col_empty = st.columns([1, 1, 1])
    
    if col_yes.button("Confirm & Submit", type="primary", use_container_width=True):
        # Add to database
        if add_data(st.session_state.pending_data):
            st.success(f"Application submitted successfully!\n\n**Audition:** {data['aud_date']}\n**Interview:** {data['interview_date']}\n\nSee you there, {data['first_name']}!")
            st.balloons()
            # Clear confirmation state
            st.session_state.show_confirmation = False
            st.session_state.pending_data = None
        else:
            st.error("Failed to submit application. Please try again or contact support.")
    
    if col_no.button("← Go Back", use_container_width=True):
        # Clear confirmation state
        st.session_state.show_confirmation = False
        st.session_state.pending_data = None
        st.rerun()