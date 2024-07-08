""" run the app"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api import create_app, register_routes
from config import Config, DevelopmentConfig

app = create_app(config_class=DevelopmentConfig)  # Use DevelopmentConfig or another appropriate config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'  # Set the database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Register all routes using the register_routes function
register_routes(app)

# Create tables based on models
from persistence.data_manager import DataManager
DataManager().create_tables()

if __name__ == "__main__":
    app.run(debug=True)
