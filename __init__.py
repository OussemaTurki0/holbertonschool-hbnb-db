""" Initialize the Flask app. """

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

# Chargement des variables d'environnement depuis le fichier .env
load_dotenv()

SQL = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()
cors = CORS()

def create_app(config_class="src.config.DevelopmentConfig") -> Flask:
    """
    Create a Flask app with the given configuration class.
    The default configuration class is DevelopmentConfig.
    """
    app = Flask(__name__)

    # Configuration de l'application
    app.config.from_object(config_class)
    app.url_map.strict_slashes = False

    register_extensions(app)

    register_handlers(app)

    return app

def register_extensions(app: Flask) -> None:
    """Register the extensions for the Flask app"""
    SQL.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})
    # Further extensions can be added here

def register_routes(app: Flask) -> None:
    """Import and register the routes for the Flask app"""

    # Import the routes here to avoid circular imports
    from controolers.users_controllers import users_bp
    from controolers.country_controllers import countries_bp
    from controolers.city_controllers import cities_bp
    from controolers.place_controllers import places_bp
    from controolers.amenity_controllers import amenities_bp
    from controolers.review_controllers import reviews_bp

    # Register the blueprints in the app
    app.register_blueprint(user_routes)
    app.register_blueprint(country_routes)
    app.register_blueprint(city_routes)
    app.register_blueprint(place_routes)
    app.register_blueprint(review_routes)
    app.register_blueprint(amenity_routes)

def register_handlers(app: Flask) -> None:
    """Register the error handlers for the Flask app."""
    app.errorhandler(404)(lambda e: (
        {"error": "Not found", "message": str(e)}, 404
    ))
    app.errorhandler(400)(lambda e: (
        {"error": "Bad request", "message": str(e)}, 400
    ))