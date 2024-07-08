#!/usr/bin/python3
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from api import db


class Amenity(BaseModel):
    """Amenity representation"""
    __tablename__ = 'amenities'
    id = Column(String(36), primary_key=True)
    name = Column(String(80), nullable=False, unique=True)
    created_at = Column(DateTime, default=db.func.current_timestamp())
    updated_at = Column(DateTime, onupdate=db.func.current_timestamp())

    def __init__(self, name: str):
        self.name = name
    def __repr__(self) -> str:
        """String representation of the object"""
        return f"<Amenity {self.id} ({self.name})>"
    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @staticmethod
    def create(data: dict) -> "Amenity":
        """Create a new amenity"""
        existing_amenity = Amenity.query.filter_by(name=data["name"]).first()
        if existing_amenity:
            raise ValueError("Amenity already exists")
        new_amenity = Amenity(name=data["name"])
        db.session.add(new_amenity)
        db.session.commit()
        return new_amenity

    @staticmethod
    def update(amenity_id: str, data: dict) -> "Amenity":
        """Update an existing amenity"""
        amenity = Amenity.query.get(amenity_id)
        if not amenity:
            return None
        if "name" in data:
            amenity.name = data["name"]
        db.session.commit()
        return amenity
