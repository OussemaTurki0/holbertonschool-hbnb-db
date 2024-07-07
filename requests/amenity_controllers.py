import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import abort, request
from models.amenity import Amenity
# handle HTTP requests and responses.

def get_all_amenities():
    amenities: list[Amenity] = Amenity.get_all()
    return [amenity.to_dict() for amenity in amenities]


def create_amenity():
    data = request.get_json()
    try:
        new_amenity = Amenity.create(data)
    except KeyError as e:
        abort(400, f"Missing field: {e}")
    except ValueError as e:
        abort(400, str(e))
    return new_amenity.to_dict(), 201


def get_amenity_by_id(amenity_id: str):
    amenity: Amenity | None = Amenity.get(amenity_id)
    if not amenity:
        abort(404, f"Amenity with ID {amenity_id} not found")
    return amenity.to_dict()


def update_amenity(amenity_id: str):
    data = request.get_json()
    modified_amenity: Amenity | None = Amenity.update(amenity_id, data)
    if not modified_amenity:
        abort(404, f"Amenity with ID {amenity_id} not found")
    return modified_amenity.to_dict()


def delete_amenity(amenity_id: str):
    if not Amenity.delete(amenity_id):
        abort(404, f"Amenity with ID {amenity_id} not found")
    return "", 204
