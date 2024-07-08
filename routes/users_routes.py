import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

"""
This script defines the routes for user-related API endpoints.
"""

from flask import Blueprint
from api.users_controllers import (
    create_user,
    delete_user,
    get_user_by_id,
    get_all_users,
    update_user,
    user_login
)

# Create a Blueprint for the user routes
users_routes = Blueprint("user_routes", __name__, url_prefix="/users")

# Define the route for getting all users
users_routes.route("/", methods=["GET"])(get_all_users)

# Define the route for creating a new user
users_routes.route("/", methods=["POST"])(create_user)

# Define the route for getting a user by ID
users_routes.route("/<user_id>", methods=["GET"])(get_user_by_id)

# Define the route for updating a user by ID
users_routes.route("/<user_id>", methods=["PUT"])(update_user)

# Define the route for deleting a user by ID
users_routes.route("/<user_id>", methods=["DELETE"])(delete_user)
# User login route
users_routes.route("/login", methods=["POST"])(user_login)