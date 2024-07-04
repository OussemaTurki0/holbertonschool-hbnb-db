"""
This script defines the routes for the cities functionality.
"""

from flask import Blueprint
from requests.city_controllers import (
    create_city,
    delete_city,
    get_city_by_id,
    get_cities,
    update_city,
)

# Create a Blueprint for city routes
city_routes = Blueprint("city_routes", __name__, url_prefix="/cities")

# Route for getting all cities
city_routes.route("/", methods=["GET"])(get_cities)

# Route for creating a new city
city_routes.route("/", methods=["POST"])(create_city)

# Route for getting a city by ID
city_routes.route("/<city_id>", methods=["GET"])(get_city_by_id)

# Route for updating a city by ID
city_routes.route("/<city_id>", methods=["PUT"])(update_city)

# Route for deleting a city by ID
city_routes.route("/<city_id>", methods=["DELETE"])(delete_city)
