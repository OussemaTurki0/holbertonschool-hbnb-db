"""
Modified Users controller module
"""

from flask import abort, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from models.user import User
from __init__ import SQL

def fetch_all_users():
    """Fetches all users"""
    users: list[User] = User.query.all()

    return [user.to_dict() for user in users]


@jwt_required()
def create_new_user():
    """Creates a new user"""
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Administration rights required"}), 403

    data = request.get_json()

    try:
        new_user = User.create(data)
    except KeyError as e:
        abort(400, f"Missing field: {e}")
    except ValueError as e:
        abort(400, str(e))

    if new_user is None:
        abort(400, "User already exists")

    return new_user.to_dict(), 201


def fetch_user_by_id(user_id: str):
    """Fetches a user by ID"""
    user = User.query.get(user_id)
    user: User | None = User.get(user_id)

    if not user:
        abort(404, f"User with ID {user_id} not found")

    return user.to_dict(), 200


@jwt_required()
def modify_user(user_id: str):
    """Modifies a user by ID"""
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Administration rights required"}), 403

    data = request.get_json()

    try:
        modified_user = User.update(user_id, data)
    except ValueError as e:
        abort(400, str(e))

    if modified_user is None:
        abort(404, f"User with ID {user_id} not found")

    return modified_user.to_dict(), 200


@jwt_required()
def remove_user(user_id: str):
    """Removes a user by ID"""
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Administration rights required"}), 403

    user = User.query.get(user_id)
    if not User.delete(user_id):
        abort(404, f"User with ID {user_id} not found")

    SQL.session.delete(user)
    SQL.session.commit()

    return "", 204
