#!/usr/bin/python3
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

SQL = SQLAlchemy()

class Amenity(BaseModel):
    """Amenity representation"""
    __tablename__ = 'amenities'
    id = SQL.Column(SQL.String(36), primary_key=True)
    name = SQL.Column(SQL.String(80), nullable=False, unique=True)
    created_at = SQL.Column(SQL.DateTime, default=SQL.func.current_timestamp())
    updated_at = SQL.Column(SQL.DateTime, onupdate=SQL.func.current_timestamp())

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
        SQL.session.add(new_amenity)
        SQL.session.commit()
        return new_amenity

    @staticmethod
    def update(amenity_id: str, data: dict) -> "Amenity":
        """Update an existing amenity"""
        amenity = Amenity.query.get(amenity_id)
        if not amenity:
            return None
        if "name" in data:
            amenity.name = data["name"]
        SQL.session.commit()
        return amenity
