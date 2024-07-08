import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

"""
This script sets up the routes for the places functionality.
"""

from flask import Blueprint
from api.place_controllers import (
    create_place,
    delete_place,
    get_place_by_id,
    get_all_places,
    update_place,
)

# Create a Blueprint for place routes
places_routes = Blueprint("place_routes", __name__, url_prefix="/places")

# Route for getting all places
places_routes.route("/", methods=["GET"])(get_all_places)

# Route for creating a new place
places_routes.route("/", methods=["POST"])(create_place)

# Route for getting a place by ID
places_routes.route("/<place_id>", methods=["GET"])(get_place_by_id)

# Route for updating a place by ID
places_routes.route("/<place_id>", methods=["PUT"])(update_place)

# Route for deleting a place by ID
places_routes.route("/<place_id>", methods=["DELETE"])(delete_place)
