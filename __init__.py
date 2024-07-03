""" Initialize the Custom Flask app. """

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

SQL = SQLAlchemy()
bcrypt= Bcrypt()
jwt = JWTManager()
cors = CORS()

def create_custom_app(config_class="config.DevelopmentConfig") -> Flask:
    """
    Create a customized Flask app using the specified configuration class.
    Default configuration class is DevelopmentConfig.
    """
    app_instance = Flask(__name__)

    # Configure the application
    app_instance.config.from_object(config_class)
    app_instance.url_map.strict_slashes = False

    register_custom_extensions(app_instance)

    register_custom_handlers(app_instance)

    return app_instance

def register_custom_extensions(app: Flask) -> None:
    """Register custom extensions for the Flask app"""
    db_instance.init_app(app)
    bcrypt_instance.init_app(app)
    jwt_manager.init_app(app)
    cors_instance.init_app(app, resources={r"/api/*": {"origins": "*"}})
    # Additional extensions can be added here

def register_custom_routes(app: Flask) -> None:
    """Import and register custom routes for the Flask app"""

    # Import routes to avoid circular dependencies
    from routes.users import users_blueprint
    from routes.countries import countries_blueprint
    from routes.cities import cities_blueprint
    from routes.places import places_blueprint
    from routes.amenities import amenities_blueprint
    from routes.reviews import reviews_blueprint
    from routes.auth import auth_blueprint

    # Register blueprints in the app
    app.register_blueprint(users_blueprint)
    app.register_blueprint(countries_blueprint)
    app.register_blueprint(cities_blueprint)
    app.register_blueprint(places_blueprint)
    app.register_blueprint(reviews_blueprint)
    app.register_blueprint(amenities_blueprint)
    app.register_blueprint(auth_blueprint)

def register_custom_handlers(app: Flask) -> None:
    """Register custom error handlers for the Flask app."""
    app.errorhandler(404)(lambda e: (
        {"error": "Not found", "message": str(e)}, 404
    ))
    app.errorhandler(400)(lambda e: (
        {"error": "Bad request", "message": str(e)}, 400
    ))
