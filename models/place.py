import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import Column, String, Integer, Float, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from flask_sqlalchemy import SQLAlchemy
from api import db


class Place(BaseModel):
    __tablename__ = 'places'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    address = Column(String(255), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)
    host_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    number_of_rooms = Column(Integer, nullable=False)
    number_of_bathrooms = Column(Integer, nullable=False)
    price_per_night = Column(Float, nullable=False)
    max_guests = Column(Integer, nullable=False)
    
    # Relationships
    host = relationship('User', back_populates='places')
    city = relationship('City', back_populates='places')
    reviews = relationship('Review', back_populates='place')
    amenities = relationship('Amenity', secondary='place_amenity_association', back_populates='places')

    def __init__(self, name, description, address, latitude, longitude, city_id, host_id, number_of_rooms, number_of_bathrooms, price_per_night, max_guests):
        super().__init__()
        self.name = name
        self.description = description
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.city_id = city_id
        self.host_id = host_id
        self.number_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests

    def __repr__(self):
        """String representation of the object"""
        return f"<Place {self.id} ({self.name})>"

    def to_dict(self):
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "address": self.address,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "city_id": self.city_id,
            "host_id": self.host_id,
            "number_of_rooms": self.number_of_rooms,
            "number_of_bathrooms": self.number_of_bathrooms,
            "price_per_night": self.price_per_night,
            "max_guests": self.max_guests,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @staticmethod
    def create(data: dict) -> "Place":
        """Create a new place"""
        from .user import User
        from .city import City

        user = User.query.get(data["host_id"])
        if not user:
            raise ValueError(f"User with ID {data['host_id']} not found")

        city = City.query.get(data["city_id"])
        if not city:
            raise ValueError(f"City with ID {data['city_id']} not found")

        new_place = Place(
            name=data["name"],
            description=data.get("description", ""),
            address=data["address"],
            latitude=float(data["latitude"]),
            longitude=float(data["longitude"]),
            city_id=data["city_id"],
            host_id=data["host_id"],
            number_of_rooms=int(data["number_of_rooms"]),
            number_of_bathrooms=int(data["number_of_bathrooms"]),
            price_per_night=float(data["price_per_night"]),
            max_guests=int(data["max_guests"])
        )

        db.session.add(new_place)
        db.session.commit()

        return new_place

    @staticmethod
    def update(place_id: str, data: dict) -> "Place | None":
        """Update an existing place"""
        place = Place.query.get(place_id)
        if not place:
            return None
        for key, value in data.items():
            setattr(place, key, value)
        db.session.commit()
        return place
