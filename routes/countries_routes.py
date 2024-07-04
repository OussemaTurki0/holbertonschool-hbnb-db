"""
This script defines the routes for the countries endpoints.
"""

from flask import Blueprint
from controolers.country_controllers import (
    get_countries,
    get_country_by_code,
    get_country_cities,
)

# Create a Blueprint for country routes
country_routes = Blueprint("country_routes", __name__, url_prefix="/countries")

# Route for getting all countries
country_routes.route("/", methods=["GET"])(get_countries)

# Route for getting a country by its code
country_routes.route("/<code>", methods=["GET"])(get_country_by_code)

# Route for getting cities in a country by its code
country_routes.route("/<code>/cities", methods=["GET"])(get_country_cities)