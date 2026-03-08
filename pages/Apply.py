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

registration_open = datetime.datetime.now() < REGISTRATION_DEADLINE

# Custom CSS for minimalistic design
st.markdown(f"""
    <style>
    /* Hide default elements */
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
    
    [data-theme="dark"] .page-title {{
        background: linear-gradient(135deg, #8b9eff 0%, #a78bfa 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    
    .page-subtitle {{
        font-size: 0.95rem;
        color: #6c757d;
        margin-bottom: 2rem;
    }}
    
    [data-theme="dark"] .page-subtitle {{
        color: #adb5bd;
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
    
    [data-theme="dark"] .review-container {{
        background: #1e1e1e;
        border: 1px solid #333;
    }}
    
    @media (prefers-color-scheme: dark) {{
        .review-container {{
            background: #1e1e1e;
            border: 1px solid #333;
        }}
    }}
    
    .review-title {{
        font-size: 1.3rem;
        font-weight: 600;
        color: #212529;
        margin-bottom: 1rem;
    }}
    
    [data-theme="dark"] .review-title {{
        color: #e9ecef;
    }}
    
    @media (prefers-color-scheme: dark) {{
        .review-title {{
            color: #e9ecef;
        }}
    }}
    
    .info-row {{
        display: flex;
        justify-content: space-between;
        padding: 0.5rem 0;
        border-bottom: 1px solid #dee2e6;
    }}
    
    [data-theme="dark"] .info-row {{
        border-bottom: 1px solid #444;
    }}
    
    @media (prefers-color-scheme: dark) {{
        .info-row {{
            border-bottom: 1px solid #444;
        }}
    }}
    
    .info-label {{
        font-weight: 500;
        color: #6c757d;
    }}
    
    [data-theme="dark"] .info-label {{
        color: #adb5bd;
    }}
    
    @media (prefers-color-scheme: dark) {{
        .info-label {{
            color: #adb5bd;
        }}
    }}
    
    .info-value {{
        color: #212529;
        text-align: right;
    }}
    
    [data-theme="dark"] .info-value {{
        color: #ffffff !important;
    }}
    
    @media (prefers-color-scheme: dark) {{
        .info-value {{
            color: #ffffff !important;
        }}
    }}
    
    /* Responsive adjustments */
    @media (max-width: 768px) {{
        .page-title {{
            font-size: 1.75rem;
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
    }}
    
    @media (max-width: 480px) {{
        .page-title {{
            font-size: 1.5rem;
        }}
        
        .logo-corner {{
            width: 80px;
        }}
        
        .status-corner {{
            font-size: 0.7rem;
            padding: 0.35rem 0.7rem;
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

if datetime.datetime.now() > REGISTRATION_DEADLINE:
    st.markdown('<div class="page-title">Registration Closed</div>', unsafe_allow_html=True)
    st.warning("Sorry! The Registration Process is now closed.")
    st.info("For inquiries, please contact your Dgroup Leader.")
else:
    # Check if we're in confirmation mode
    show_confirmation = st.session_state.get("show_confirmation", False)
    submission_success = st.session_state.get("submission_success", False)

    if submission_success:
        data = st.session_state.get("submitted_data", {})
        first_name = data.get("first_name", "there")
        aud_date = data.get("aud_date", "")
        interview_date = data.get("interview_date", "")

        st.markdown(f"""
            <div style="text-align: center; padding: 3rem 1rem;">
                <div style="font-size: 3.5rem; margin-bottom: 1rem;">🎉</div>
                <div class="page-title" style="font-size: 2.2rem; margin-bottom: 0.5rem;">You're all set, {first_name}!</div>
                <div class="page-subtitle">Your audition application has been submitted successfully.</div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
            <style>
                .success-summary-card {{
                    border: 1px solid #e9ecef;
                    border-radius: 12px;
                    padding: 1.25rem 1.5rem;
                    max-width: 420px;
                    margin: 0 auto 2rem auto;
                }}
                [data-theme="dark"] .success-summary-card,
                @media (prefers-color-scheme: dark) {{
                    .success-summary-card {{ border-color: #2a2a2a; }}
                }}
                .success-summary-row {{
                    display: flex;
                    justify-content: space-between;
                    padding: 0.5rem 0;
                }}
                .success-summary-row.bordered {{
                    border-bottom: 1px solid #f0f0f0;
                }}
                [data-theme="dark"] .success-summary-row.bordered {{
                    border-bottom-color: #2a2a2a;
                }}
                @media (prefers-color-scheme: dark) {{
                    .success-summary-row.bordered {{ border-bottom-color: #2a2a2a; }}
                }}
                .success-summary-label {{
                    font-size: 0.8rem;
                    font-weight: 600;
                    color: #9ca3af;
                    text-transform: uppercase;
                    letter-spacing: 0.05em;
                }}
                .success-summary-value {{
                    font-size: 0.92rem;
                    font-weight: 500;
                    color: #1f2937 !important;
                }}
                [data-theme="dark"] .success-summary-value {{
                    color: #f3f4f6 !important;
                }}
                @media (prefers-color-scheme: dark) {{
                    .success-summary-value {{ color: #f3f4f6 !important; }}
                }}
            </style>
            <div class="success-summary-card">
                <div class="success-summary-row bordered">
                    <span class="success-summary-label">Audition</span>
                    <span class="success-summary-value">{aud_date}</span>
                </div>
                <div class="success-summary-row">
                    <span class="success-summary-label">Interview</span>
                    <span class="success-summary-value">{interview_date}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown('<p style="text-align: center; color: #6c757d; font-size: 0.9rem; margin-bottom: 0.75rem;">Please save the audition playlist below for future reference.</p>', unsafe_allow_html=True)

        col_left, col_center, col_right = st.columns([1, 2, 1])
        with col_center:
            st.link_button(
                "▶  View Audition Playlist on YouTube",
                "https://youtube.com/playlist?list=PLOzqg8hRX-XGd7X8JeWTJpWdAYE4kaBOj&si=yWbO8nPyOPzhafdX",
                use_container_width=True,
                type="primary"
            )

    elif not show_confirmation:
        # Page header
        st.markdown('<div class="page-title">Audition Application</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-subtitle">Elevate Exalt Feliz</div>', unsafe_allow_html=True)

        # Get existing data from session state if available (to preserve form data)
        existing_data = st.session_state.get("pending_data", {})

        # Personal Information Section
        st.markdown('<div class="section-header">Personal Information</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        first_name = col1.text_input(
            "First Name *", 
            placeholder="Enter your first name",
            value=existing_data.get("first_name", "")
        )
        last_name = col1.text_input(
            "Last Name *", 
            placeholder="Enter your last name",
            value=existing_data.get("last_name", "")
        )
        age = col2.number_input(
            "Age", 
            min_value=0, 
            max_value=100, 
            value=existing_data.get("age", 0)
        )
        phone = col2.text_input(
            "Phone Number", 
            placeholder="09XX XXX XXXX",
            value=existing_data.get("phone", "")
        )

        st.markdown('<div class="section-header">Contact</div>', unsafe_allow_html=True)
        
        col3, col4 = st.columns(2)
        email = col3.text_input(
            "Email Address *", 
            placeholder="your.email@example.com",
            value=existing_data.get("email", "")
        )
        dleader = col4.text_input(
            "Dgroup Leader *", 
            placeholder="Leader's name",
            value=existing_data.get("dleader", "")
        )

        st.markdown('<div class="section-header">Audition Details</div>', unsafe_allow_html=True)
        
        category_options = ["Band", "Singer"]
        category_index = None
        if existing_data.get("category") in category_options:
            category_index = category_options.index(existing_data.get("category"))
        
        category = st.selectbox(
            "Category *", 
            category_options,
            index=category_index,
            placeholder="Select a category...",
            help="Select your audition category"
        )

        if category == "Band":
            instrument_options = ["Acoustic Guitar", "Electric Guitar", "Bass Guitar", "Drums", "Keyboard"]
            instrument_index = None
            if existing_data.get("instrument") in instrument_options:
                instrument_index = instrument_options.index(existing_data.get("instrument"))
            
            instrument = st.selectbox(
                "Instrument *",
                instrument_options,
                index=instrument_index,
                placeholder="Select an instrument...",
                help="Select your primary instrument"
            )
        elif category == "Singer":
            instrument = "Vocals"
        else:
            instrument = None

        st.markdown('<div class="section-header">Schedule</div>', unsafe_allow_html=True)
        
        col5, col6 = st.columns(2)
        
        with col5:
            all_audition_dates = ["March 21, 4:30PM"]
            
            current_datetime = datetime.datetime.now()
            available_audition_dates = []
            
            for date_str in all_audition_dates:
                if "March 21" in date_str:
                    date_obj = datetime.datetime(2026, 3, 21, 16, 30)
                
                if date_obj > current_datetime:
                    available_audition_dates.append(date_str)
            
            if available_audition_dates:
                aud_date_index = None
                if existing_data.get("aud_date") in available_audition_dates:
                    aud_date_index = available_audition_dates.index(existing_data.get("aud_date"))
                
                aud_date = st.selectbox(
                    "Audition Date *", 
                    available_audition_dates,
                    index=aud_date_index,
                    placeholder="Select a date...",
                    help="Choose your preferred audition date"
                )
            else:
                st.warning("No upcoming audition dates available.")
                aud_date = None
        
        with col6:
            if aud_date:
                if aud_date == "March 21, 4:30PM":
                    interview_options_list = ["March 28, 5:00PM"]
                
                interview_index = None
                if existing_data.get("interview_date") in interview_options_list:
                    interview_index = interview_options_list.index(existing_data.get("interview_date"))
                
                interview_date = st.selectbox(
                    "Interview Date *", 
                    interview_options_list,
                    index=interview_index,
                    placeholder="Select a date...",
                    help="Choose your preferred interview date" if len(interview_options_list) > 1 else "Available interview date for this audition"
                )
            else:
                interview_date = None

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

        col_left, col_center, col_right = st.columns([1, 2, 1])
        with col_center:
            submit_clicked = st.button("Continue to Review", type="primary", use_container_width=True)

        if submit_clicked:
            if not first_name or not last_name or not email or not dleader:
                st.error("Please fill in all required fields (marked with *)!")
            elif not category:
                st.error("Please select a category!")
            elif category == "Band" and not instrument:
                st.error("Please select an instrument!")
            elif not aud_date:
                st.error("Please select an audition date!")
            elif not interview_date:
                st.error("Please select an interview date!")
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
    else:
        # Confirmation/Review mode
        data = st.session_state.pending_data
        
        st.markdown('<div class="page-title">Review Your Application</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-subtitle">Please confirm your details before submitting</div>', unsafe_allow_html=True)
        
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
        
        st.warning("⚠️ Please review your information carefully. Once submitted, changes cannot be made.")
        
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        
        col_yes, col_no, col_empty = st.columns([1, 1, 1])
        
        if col_yes.button("Submit", type="primary", use_container_width=True):
            if add_data(st.session_state.pending_data):
                st.session_state.submitted_data = st.session_state.pending_data
                st.session_state.submission_success = True
                st.session_state.show_confirmation = False
                st.session_state.pending_data = None
                st.rerun()
            else:
                st.error("Failed to submit application. Please try again or contact support.")
        
        if col_no.button("← Edit Application", use_container_width=True):
            st.session_state.show_confirmation = False
            st.rerun()