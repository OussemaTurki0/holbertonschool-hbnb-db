#!/usr/bin/python3
from models.basemodel import Basemodel
from sqlalchemy import Column, String, Integer, Boolean
import bcrpyt


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    review = Column(String, )
    hashed_password = Column(String, nullable=False)
	is_admin = Column(Boolean, default=False)

	def set_password(self, password):
        """Hash the password and store it."""
        salt = bcrypt.gensalt()
        self.hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    
	def __init__(self, first_name, last_name, email, hashed_password):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.set_password_password(password)
		self.is_admin = is_admin