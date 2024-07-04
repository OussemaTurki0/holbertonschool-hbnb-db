"""
This script defines the routes for user-related API endpoints.
"""

from flask import Blueprint
from requests.users_controllers import (
    create_user,
    delete_user,
    get_user_by_id,
    get_users,
    update_user,
)

# Create a Blueprint for the user routes
user_routes = Blueprint("user_routes", __name__, url_prefix="/users")

# Define the route for getting all users
user_routes.route("/", methods=["GET"])(get_users)

# Define the route for creating a new user
user_routes.route("/", methods=["POST"])(create_user)

# Define the route for getting a user by ID
user_routes.route("/<user_id>", methods=["GET"])(get_user_by_id)

# Define the route for updating a user by ID
user_routes.route("/<user_id>", methods=["PUT"])(update_user)

# Define the route for deleting a user by ID
user_routes.route("/<user_id>", methods=["DELETE"])(delete_user)
