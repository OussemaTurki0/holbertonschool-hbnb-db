import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import abort, request
from models.place import Place
# handle HTTP requests and responses.

def get_all_places():
    places: list[Place] = Place.get_all()
    return [place.to_dict() for place in places], 200


def create_place():
    data = request.get_json()
    try:
        new_place = Place.create(data)
    except KeyError as e:
        abort(400, f"Missing field: {e}")
    except ValueError as e:
        abort(404, str(e))
    return new_place.to_dict(), 201


def get_place_by_id(place_id: str):
    place: Place | None = Place.get(place_id)
    if not place:
        abort(404, f"Place with ID {place_id} not found")
    return place.to_dict(), 200


def update_place(place_id: str):
    data = request.get_json()
    try:
        modified_place: Place | None = Place.update(place_id, data)
    except ValueError as e:
        abort(400, str(e))
    if not modified_place:
        abort(404, f"Place with ID {place_id} not found")
    return modified_place.to_dict(), 200


def delete_place(place_id: str):
    if not Place.delete(place_id):
        abort(404, f"Place with ID {place_id} not found")
    return "", 204
