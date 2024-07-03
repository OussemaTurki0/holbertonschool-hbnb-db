"""
Modified Cities controller module
"""

from flask import request, abort
from models.city import City


def fetch_all_cities():
    """Fetches all cities"""
    cities: list[City] = City.get_all()

    return [city.to_dict() for city in cities]


def create_new_city():
    """Creates a new city"""
    data = request.get_json()

    try:
        new_city = City.create(data)
    except KeyError as e:
        abort(400, f"Missing field: {e}")
    except ValueError as e:
        abort(400, str(e))

    return new_city.to_dict(), 201


def fetch_city_by_id(city_id: str):
    """Fetches a city by its ID"""
    city: City | None = City.get(city_id)

    if not city:
        abort(404, f"City with ID {city_id} not found")

    return city.to_dict()


def modify_city(city_id: str):
    """Modifies a city by its ID"""
    data = request.get_json()

    try:
        modified_city: City | None = City.update(city_id, data)
    except ValueError as e:
        abort(400, str(e))

    if not modified_city:
        abort(404, f"City with ID {city_id} not found")

    return modified_city.to_dict()


def remove_city(city_id: str):
    """Removes a city by its ID"""
    if not City.delete(city_id):
        abort(404, f"City with ID {city_id} not found")

    return "", 204
