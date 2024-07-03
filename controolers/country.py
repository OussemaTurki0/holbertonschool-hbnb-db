"""
Modified Countries controller module
"""

from flask import abort
from models.city import City
from models.country import Country


def fetch_all_countries():
    """Fetches all countries"""
    countries: list[Country] = Country.get_all()

    return [country.to_dict() for country in countries]


def fetch_country_by_code(code: str):
    """Fetches a country by its code"""
    country: Country | None = Country.get(code)

    if not country:
        abort(404, f"Country with code {code} not found")

    return country.to_dict()


def fetch_country_cities(code: str):
    """Fetches all cities for a specific country by its code"""
    country: Country | None = Country.get(code)

    if not country:
        abort(404, f"Country with code {code} not found")

    cities: list[City] = City.get_all()

    country_cities = [
        city.to_dict() for city in cities if city.country_code == country.code
    ]

    return country_cities
