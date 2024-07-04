from flask import abort, request
from models.review import Review
# handle HTTP requests and responses.

def fetch_all_reviews():
    reviews = Review.get_all()
    return [review.to_dict() for review in reviews], 200


def post_review(place_id: str):
    data = request.get_json()
    if "author_id" not in data:
        abort(400, "Missing field: author_id")
    try:
        new_review = Review.create(data | {"place_id": place_id})
    except KeyError as e:
        abort(400, f"Missing field: {e}")
    except ValueError as e:
        abort(400, str(e))
    return new_review.to_dict(), 201


def fetch_reviews_by_place(place_id: str):
    reviews = Review.get_all()
    return [
        review.to_dict() for review in reviews if review.place_id == place_id
    ], 200


def fetch_reviews_by_user(user_id: str):
    reviews = Review.get_all()
    return [
        review.to_dict() for review in reviews if review.user_id == user_id
    ], 200


def fetch_review_by_id(review_id: str):
    review: Review | None = Review.get(review_id)
    if not review:
        abort(404, f"Review with ID {review_id} not found")
    return review.to_dict(), 200


def modify_review(review_id: str):
    data = request.get_json()
    try:
        modified_review: Review | None = Review.update(review_id, data)
    except ValueError as e:
        abort(400, str(e))
    if not modified_review:
        abort(404, f"Review with ID {review_id} not found")
    return modified_review.to_dict(), 200


def remove_review(review_id: str):
    if not Review.delete(review_id):
        abort(404, f"Review with ID {review_id} not found")
    return "", 204
