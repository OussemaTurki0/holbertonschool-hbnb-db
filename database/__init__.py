from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

DATA_BASE = "sqlite:///./data.db"

# Create the SQLAlchemy engine and session
engine = create_engine(DATA_BASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
