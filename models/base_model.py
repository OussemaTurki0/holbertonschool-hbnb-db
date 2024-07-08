from abc import abstractmethod
from api import db
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datetime import datetime
from typing import Any, Optional
import uuid
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True  # This ensures SQLAlchemy doesn't try to create a table for this class

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def get(cls, id: str) -> Optional["Any"]:
        return db.session.query(cls).get(id)

    @classmethod
    def get_all(cls) -> list["Any"]:
        from api import db
        return db.session.query(cls).all()

    @classmethod
    def delete(cls, id: str) -> bool:
        from api import db
        obj = cls.get(id)
        if obj:
            db.session.delete(obj)
            db.session.commit()
            return True
        return False

    @abstractmethod
    def to_dict(self) -> dict:
        pass

    @staticmethod
    @abstractmethod
    def create(data: dict) -> Any:
        pass

    @staticmethod
    @abstractmethod
    def update(entity_id: str, data: dict) -> Optional[Any]:
        pass
