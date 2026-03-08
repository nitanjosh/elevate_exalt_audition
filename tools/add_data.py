import pandas as pd
import streamlit as st
from sqlalchemy import text
from tools.db import engine

def init_df():
    """Initialize session state dataframe (optional for display)"""
    if "df" not in st.session_state:
        st.session_state.df = pd.DataFrame(
            columns=[
                "first_name","last_name","age","phone","email",
                "dleader","materials","category","instrument","aud_date","interview_date"
            ]
        )

def add_data(data: dict):
    """Add applicant data to the database"""
    try:
        with engine.connect() as conn:
            query = text("""
                INSERT INTO auditionees 
                (first_name, last_name, age, phone, email, dleader, materials, category, instrument, aud_date, interview_date)
                VALUES 
                (:first_name, :last_name, :age, :phone, :email, :dleader, :materials, :category, :instrument, :aud_date, :interview_date)
            """)
            
            conn.execute(query, data)
            conn.commit()
        
        # Optionally update session state for display
        new_row = pd.DataFrame([data])
        st.session_state.df = pd.concat(
            [st.session_state.df, new_row],
            ignore_index=True
        )
        
        return True
        
    except Exception as e:
        st.error(f"Database error: {e}")
        return False

def get_all_applicants():
    """Retrieve all applicants from database"""
    try:
        with engine.connect() as conn:
            query = text("SELECT * FROM auditionees ORDER BY created_at DESC")
            result = conn.execute(query)
            df = pd.DataFrame(result.fetchall(), columns=result.keys())
        return df
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame()