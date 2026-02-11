# src/tools/db.py
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL not set. Please set it in your .env or Streamlit Secrets.")

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL not set. Please set it in your .env or Streamlit Secrets.")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

#Connection test
try:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
        print("Database connected successfully!")
except Exception as e:
    print("Database connection failed:", e)

# Authentication function
def verify_admin(username, password):
    """Verify admin credentials from database"""
    try:
        with engine.connect() as conn:
            query = text("""
                SELECT * FROM admin 
                WHERE username = :username AND password = :password
            """)
            result = conn.execute(query, {"username": username, "password": password})
            return result.fetchone() is not None
    except Exception as e:
        print(f"Authentication error: {e}")
        return False
try:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
        print("Database connected successfully!")
except Exception as e:
    print("Database connection failed:", e)