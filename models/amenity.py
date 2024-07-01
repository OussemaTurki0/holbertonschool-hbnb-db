#!/usr/bin/python3
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Amenity(BaseModel):
    __tablename__ = 'amenities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    place_id = Column(Integer, ForeignKey('places.id'), nullable=False)
    place = relationship('Place', back_populates='amenities')

    def __init__(self, name, place_id):
        super().__init__()
        self.name = name
        self.place_id = place_id
