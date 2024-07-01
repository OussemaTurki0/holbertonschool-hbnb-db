#!/usr/bin/python3
from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from models.base_model import BaseModel

class Review(BaseModel):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    place_id = Column(Integer, ForeignKey('places.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    text = Column(Text, nullable=False)
    user = relationship('User', back_populates='reviews')  # Many-to-One: Each review belongs to one user
    place = relationship('Place', back_populates='reviews')  # Many-to-One: Each review is for one place

    def __init__(self, user_id, place_id, rating, text):
        super().__init__()
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.text = text
