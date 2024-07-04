"""
This script defines the routes for the amenities functionality.
"""

from flask import Blueprint
from controolers.amenity_controllers import (
    create_amenity,
    delete_amenity,
    get_amenity_by_id,
    get_amenities,
    update_amenity,
)

# Create a Blueprint for amenity routes
amenity_routes = Blueprint("amenity_routes", __name__, url_prefix="/amenities")

# Route for getting all amenities
amenity_routes.route("/", methods=["GET"])(get_amenities)

# Route for creating a new amenity
amenity_routes.route("/", methods=["POST"])(create_amenity)

# Route for getting an amenity by ID
amenity_routes.route("/<amenity_id>", methods=["GET"])(get_amenity_by_id)

# Route for updating an amenity by ID
amenity_routes.route("/<amenity_id>", methods=["PUT"])(update_amenity)

# Route for deleting an amenity by ID
amenity_routes.route("/<amenity_id>", methods=["DELETE"])(delete_amenity)
