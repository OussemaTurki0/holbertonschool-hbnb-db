#!/usr/bin/python3
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

SQL = SQLAlchemy()

class City(BaseModel):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    country_id = Column(Integer, ForeignKey('countries.id'), nullable=False)
    country = relationship('Country', back_populates='cities')

    def __init__(self, name, country_id):
        super().__init__()
        self.name = name
        self.country_id = country_id

    def __repr__(self):
        """String representation of the object"""
        return f"<City {self.id} ({self.name})>"

    def to_dict(self):
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.name,
            "country_id": self.country_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @staticmethod
    def create(data):
        """Create a new city"""
        from .country import Country  # Adjust this based on your actual import structure
        country = Country.query.get(data["country_id"])
        if not country:
            raise ValueError("Country not found")
        new_city = City(name=data["name"], country_id=data["country_id"])
        SQL.session.add(new_city)
        SQL.session.commit()

        return new_city

    @staticmethod
    def update(city_id, data):
        """Update an existing city"""
        city = City.query.get(city_id)
        if not city:
            raise ValueError("City not found")
        if "name" in data:
            city.name = data["name"]
        if "country_id" in data:
            city.country_id = data["country_id"]
        SQL.session.commit()
        return city
