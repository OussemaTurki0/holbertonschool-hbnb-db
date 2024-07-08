import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

"""
This script sets up the routes for the reviews functionality.
"""

from flask import Blueprint
from api.review_controllers import (
    create_review,
    delete_review,
    get_reviews_from_place,
    get_reviews_from_user,
    get_review_by_id,
    get_all_reviews,
    update_review,
)

# Create a Blueprint for review routes
reviews_routes = Blueprint("review_routes", __name__)

# Route for creating a review for a specific place
reviews_routes.route("/places/<place_id>/reviews", methods=["POST"])(create_review)

# Route for getting reviews for a specific place
reviews_routes.route("/places/<place_id>/reviews")(get_reviews_from_place)

# Route for getting reviews by a specific user
reviews_routes.route("/users/<user_id>/reviews")(get_reviews_from_user)

# Route for getting all reviews
reviews_routes.route("/reviews", methods=["GET"])(get_all_reviews)

# Route for getting a review by ID
reviews_routes.route("/reviews/<review_id>", methods=["GET"])(get_review_by_id)

# Route for updating a review by ID
reviews_routes.route("/reviews/<review_id>", methods=["PUT"])(update_review)

# Route for deleting a review by ID
reviews_routes.route("/reviews/<review_id>", methods=["DELETE"])(delete_review)
