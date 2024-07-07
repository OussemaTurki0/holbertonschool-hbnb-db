import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from app import db, app

bcrypt = Bcrypt(app)


class User(BaseModel):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(120), unique=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    password_hash = Column(String(128), nullable=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=SQL.func.current_timestamp())
    updated_at = Column(DateTime, onupdate=SQL.func.current_timestamp())
    places = relationship("Place", back_populates="host")
    reviews = relationship("Review", back_populates="user")
    #Primary=key(ensures that each id value is unique and cannot be duplicated within the table.)
    #autoincrement=True(ensuring that each row gets a unique identifier without needing manual assignment.)
    # Relationships
    
    def __init__(self, email, first_name, last_name, password, is_admin=False):
        super().__init__()
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.set_password(password)
        self.is_admin = is_admin

    def __repr__(self):
        """String representation of the object"""
        return f"<User {self.id} ({self.email})>"

    def to_dict(self):
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "is_admin": self.is_admin
        }

    def set_password(self, password):
        """Hash the password and store it."""
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    
    def check_password(self, password):
        """Check if the password matches the stored hash."""
        return bcrypt.check_password_hash(self.password_hash, password)

    @staticmethod
    def create(user_data):
        """Create a new user"""
        existing_user = User.query.filter_by(email=user_data["email"]).first()
        if existing_user:
            raise ValueError("User already exists")
        new_user = User(
            email=user_data["email"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            password=user_data["password"],
            is_admin=user_data.get("is_admin", False)
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def update(user_id, data):
        """Update an existing user"""
        user = User.query.get(user_id)
        if not user:
            return None
        if "email" in data:
            user.email = data["email"]
        if "first_name" in data:
            user.first_name = data["first_name"]
        if "last_name" in data:
            user.last_name = data["last_name"]
        if "password" in data:
            user.set_password(data["password"])
        if "is_admin" in data:
            user.is_admin = data["is_admin"]
        db.session.commit()
        return user
