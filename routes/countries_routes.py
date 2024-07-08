import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

"""
This script defines the routes for the countries endpoints.
"""

from flask import Blueprint
from api.country_controllers import (
    get_all_countries,
    get_country_by_code,
    get_country_cities,
)

# Create a Blueprint for country routes
countries_routes = Blueprint("country_routes", __name__, url_prefix="/countries")

# Route for getting all countries
countries_routes.route("/", methods=["GET"])(get_all_countries)

# Route for getting a country by its code
countries_routes.route("/<code>", methods=["GET"])(get_country_by_code)

# Route for getting cities in a country by its code
countries_routes.route("/<code>/cities", methods=["GET"])(get_country_cities)
