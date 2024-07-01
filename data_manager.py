from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base

# Replace 'sqlite:///your_database.db' with your actual database connection string
DATABASE_URL = 'sqlite:///your_database.db'

# Create engine and session
engine = create_engine(DATABASE_URL, echo=True)  # Set echo to True for debugging
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
session = Session()

def create_tables():
    """Create database tables."""
    Base.metadata.create_all(engine)

def get_session():
    """Get current session."""
    return session
