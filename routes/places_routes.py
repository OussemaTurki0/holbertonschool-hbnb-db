"""
This script sets up the routes for the places functionality.
"""

from flask import Blueprint
from requests.place_controllers import (
    create_place,
    delete_place,
    get_place_by_id,
    get_all_places,
    update_place,
)

# Create a Blueprint for place routes
place_routes = Blueprint("place_routes", __name__, url_prefix="/places")

# Route for getting all places
place_routes.route("/", methods=["GET"])(get_all_places)

# Route for creating a new place
place_routes.route("/", methods=["POST"])(create_place)

# Route for getting a place by ID
place_routes.route("/<place_id>", methods=["GET"])(get_place_by_id)

# Route for updating a place by ID
place_routes.route("/<place_id>", methods=["PUT"])(update_place)

# Route for deleting a place by ID
place_routes.route("/<place_id>", methods=["DELETE"])(delete_place)
