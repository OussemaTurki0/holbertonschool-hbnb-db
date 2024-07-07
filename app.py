""" run the app"""

from flask import Flask
from flask_jwt_extended import JWTManager
from requests.__init__ import register_routes
from flask_sqlalchemy import SQLAlchemy
from requests.__init__ import create_app, db, jwt
from config import Config, DevelopmentConfig

# Initialize the Flask application using create_app() from __init__.py
app = create_app()
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)

# Register all routes using the register_routes function
register_routes(app)

# Create tables based on models
from persistence.datamanager import DataManager
DataManager().create_tables()

if __name__ == "__main__":
    app.run(debug=True)
