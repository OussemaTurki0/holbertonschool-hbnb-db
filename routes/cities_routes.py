import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

"""
This script defines the routes for the cities functionality.
"""

from flask import Blueprint
from api.city_controllers import (
    create_city,
    delete_city,
    get_city_by_id,
    get_all_cities,
    update_city,
)

# Create a Blueprint for city routes
cities_routes = Blueprint("city_routes", __name__, url_prefix="/cities")

# Route for getting all cities
cities_routes.route("/", methods=["GET"])(get_all_cities)

# Route for creating a new city
cities_routes.route("/", methods=["POST"])(create_city)

# Route for getting a city by ID
cities_routes.route("/<city_id>", methods=["GET"])(get_city_by_id)

# Route for updating a city by ID
cities_routes.route("/<city_id>", methods=["PUT"])(update_city)

# Route for deleting a city by ID
city_routes.route("/<city_id>", methods=["DELETE"])(delete_city)
