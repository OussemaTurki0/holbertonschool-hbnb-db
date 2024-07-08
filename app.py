""" run the app"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from api import create_app, register_routes
from config import DevelopmentConfig
from persistence.data_manager import DataManager

data_manager = DataManager()
data_manager.create_tables()

# Use DevelopmentConfig or another appropriate config
app = create_app(config_class=DevelopmentConfig)
# Set the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Register all routes using the register_routes function
register_routes(app)

# Create tables based on models

if __name__ == "__main__":
    app.run(debug=True, port=5002)
