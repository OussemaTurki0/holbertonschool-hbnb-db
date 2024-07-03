"""
Modified Amenity controller module
"""

from flask import abort, request
from models.amenity import Amenity


def fetch_all_amenities():
    """Fetches all amenities"""
    amenities: list[Amenity] = Amenity.get_all()

    return [amenity.to_dict() for amenity in amenities]


def create_new_amenity():
    """Creates a new amenity"""
    data = request.get_json()

    try:
        new_amenity = Amenity.create(data)
    except KeyError as e:
        abort(400, f"Missing field: {e}")
    except ValueError as e:
        abort(400, str(e))

    return new_amenity.to_dict(), 201


def fetch_amenity_by_id(amenity_id: str):
    """Fetches an amenity by its ID"""
    amenity: Amenity | None = Amenity.get(amenity_id)

    if not amenity:
        abort(404, f"Amenity with ID {amenity_id} not found")

    return amenity.to_dict()


def modify_amenity(amenity_id: str):
    """Modifies an amenity by its ID"""
    data = request.get_json()

    modified_amenity: Amenity | None = Amenity.update(amenity_id, data)

    if not modified_amenity:
        abort(404, f"Amenity with ID {amenity_id} not found")

    return modified_amenity.to_dict()


def remove_amenity(amenity_id: str):
    """Removes an amenity by its ID"""
    if not Amenity.delete(amenity_id):
        abort(404, f"Amenity with ID {amenity_id} not found")

    return "", 204
