#!/usr/bin/python3
from models.basemodel import Basemodel
from sqlalchemy import Column, String, Integer, ForeignKey

class Country(Base):
	__tablename__ = 'countries'

	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String, nullable=False)
	city_id = Column(Integer, ForeignKey('cities.id'))

    def __init__(self, name, city_id):
        super().__init__()
        self.name = name
        self.city_id = city_id