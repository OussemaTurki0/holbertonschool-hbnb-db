import sys
import os
from flask import Flask
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from config import Config

db = SQLAlchemy()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

def register_routes(app: Flask):
    # Import your blueprints
    from routes import user_routes, place_routes, review_routes, countries_routes, cities_routes, amenities_routes
    # Register blueprints
    app.register_blueprint(user_routes)
    app.register_blueprint(place_routes)
    app.register_blueprint(review_routes)
    app.register_blueprint(amenities_routes)
    app.register_blueprint(countries_routes)
    app.register_blueprint(cities_routes)


    return app
