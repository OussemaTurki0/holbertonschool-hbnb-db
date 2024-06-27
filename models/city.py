#!/usr/bin/python3
from models.basemodel import Basemodel
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    country_id = Column(Integer, ForeignKey('countries.id'), nullable=False)

	def __init__(self, name, country_id):
        super().__init__()
		self.name = name
		self.country_id = country_id