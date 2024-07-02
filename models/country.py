#!/usr/bin/python3
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Country(BaseModel):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    cities = relationship('City', back_populates='country')

    def __init__(self, name):
        super().__init__()
        self.name = name
