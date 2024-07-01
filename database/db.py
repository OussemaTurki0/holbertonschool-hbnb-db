from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATA_BASE = "sqlite:///./data.db"

engine = create_engine(DATA_BASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
