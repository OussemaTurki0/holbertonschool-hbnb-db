"""
Modified Places controller module
"""

from flask import abort, request
from models.place import Place


def fetch_all_places():
    """Fetches all places"""
    places: list[Place] = Place.get_all()

    return [place.to_dict() for place in places], 200


def create_new_place():
    """Creates a new place"""
    data = request.get_json()

    try:
        new_place = Place.create(data)
    except KeyError as e:
        abort(400, f"Missing field: {e}")
    except ValueError as e:
        abort(404, str(e))

    return new_place.to_dict(), 201


def fetch_place_by_id(place_id: str):
    """Fetches a place by its ID"""
    place: Place | None = Place.get(place_id)

    if not place:
        abort(404, f"Place with ID {place_id} not found")

    return place.to_dict(), 200


def modify_place(place_id: str):
    """Modifies a place by its ID"""
    data = request.get_json()

    try:
        modified_place: Place | None = Place.update(place_id, data)
    except ValueError as e:
        abort(400, str(e))

    if not modified_place:
        abort(404, f"Place with ID {place_id} not found")

    return modified_place.to_dict(), 200


def remove_place(place_id: str):
    """Removes a place by its ID"""
    if not Place.delete(place_id):
        abort(404, f"Place with ID {place_id} not found")

    return "", 204
