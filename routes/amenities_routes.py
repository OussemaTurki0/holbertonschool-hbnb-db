import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

"""
This script defines the routes for the amenities functionality.
"""

from flask import Blueprint
from api.amenity_controllers import (
    create_amenity,
    delete_amenity,
    get_amenity_by_id,
    get_all_amenities,
    update_amenity,
)

# Create a Blueprint for amenity routes
amenities_routes = Blueprint("amenity_routes", __name__, url_prefix="/amenities")

# Route for getting all amenities
amenities_routes.route("/", methods=["GET"])(get_amenities)

# Route for creating a new amenity
amenities_routes.route("/", methods=["POST"])(create_amenity)

# Route for getting an amenity by ID
amenities_routes.route("/<amenity_id>", methods=["GET"])(get_amenity_by_id)

# Route for updating an amenity by ID
amenities_routes.route("/<amenity_id>", methods=["PUT"])(update_amenity)

# Route for deleting an amenity by ID
amenity_routes.route("/<amenity_id>", methods=["DELETE"])(delete_amenity)
