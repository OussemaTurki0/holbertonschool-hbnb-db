from flask import Blueprint
from routes.users import user_routes
from routes.places import place_routes
from routes.reviews import review_routes
from routes.countries import countries_routes
from routes.cities import cities_routes
from routes.amenities import amenities_routes

# Register all blueprints
def register_routes(app):
    app.register_blueprint(user_routes)
    app.register_blueprint(place_routes)
    app.register_blueprint(review_routes)
    app.register_blueprint(amenities_routes)
    app.register_blueprint(countries_routes)
    app.register_blueprint(cities_routes)
