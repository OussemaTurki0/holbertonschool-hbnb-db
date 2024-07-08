import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from config import Config

# Initialize Flask extensions
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

    return app

def register_routes(app):
    # Import your blueprints here to avoid circular imports
    from routes.users_routes import users_routes
    from routes.places_routes import places_routes
    from routes.reviews_routes import reviews_routes
    from routes.amenities_routes import amenities_routes
    from routes.countries_routes import countries_routes
    from routes.cities_routes import cities_routes

    # Register blueprints
    app.register_blueprint(users_routes)
    app.register_blueprint(places_routes)
    app.register_blueprint(reviews_routes)
    app.register_blueprint(amenities_routes)
    app.register_blueprint(countries_routes)
    app.register_blueprint(cities_routes)

    return app
