#!/usr/bin/python3
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

class Place(BaseModel):
    __tablename__ = 'places'
    
    place_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    address = Column(String)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)
    host_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    number_of_rooms = Column(Integer, nullable=False)
    number_of_bathrooms = Column(Integer, nullable=False)
    price_per_night = Column(Float, nullable=False)
    max_guests = Column(Integer, nullable=False)
    host = relationship("User", back_populates="places")  # Many-to-One: Each place has one host
    amenities = relationship("Amenity", back_populates="place")  # One-to-Many: One place can have multiple amenities
    reviews = relationship("Review", back_populates="place")  # One-to-Many: One place can have multiple reviews

    def __init__(self, name, description, address, city_id, host_id, number_of_rooms, number_of_bathrooms, price_per_night, max_guests):
        super().__init__()
        self.name = name
        self.description = description
        self.address = address
        self.city_id = city_id
        self.host_id = host_id
        self.number_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
