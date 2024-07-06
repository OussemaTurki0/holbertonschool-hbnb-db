from flask import Blueprint
from .users import user_routes
from .places import place_routes
from .reviews import review_routes
from .countries import countries_routes
from .cities import cities_routes
from .amenities import amenities_routes

# Register all blueprints
def register_routes(app):
    app.register_blueprint(user_routes)
    app.register_blueprint(place_routes)
    app.register_blueprint(review_routes)
    app.register_blueprint(amenities_routes)
    app.register_blueprint(countries_routes)
    app.register_blueprint(cities_routes)
