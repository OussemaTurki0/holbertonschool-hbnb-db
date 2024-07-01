from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy instance
db = SQLAlchemy()

# Database URL for SQLite (assuming you have a 'data.db' file in your current directory)
DATABASE_URL = "sqlite:///./data.db"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a SessionLocal class to handle the session connection
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
