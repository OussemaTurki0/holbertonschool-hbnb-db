import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import abort, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from flask_jwt_extended import create_access_token
from models.user import User
from __init__ import db
# handle HTTP requests and responses.

def user_login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"msg": "Missing email or password"}), 400

    user = User.query.filter_by(email=email).first()

    if not user or not user.check_password(password):
        return jsonify({"msg": "Invalid email or password"}), 401

    if not user.is_admin:
        return jsonify({"msg": "Admin credentials required"}), 403

    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200

def get_all_users():
    users = User.query.all()
    return [user.to_dict() for user in users]

@jwt_required()
def create_user():
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


def get_user_by_id(user_id: str):
    user = User.query.get(user_id)
    if not user:
        abort(404, f"User with ID {user_id} not found")
    return user.to_dict(), 200


@jwt_required()
def update_user(user_id: str):
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
def delete_user(user_id: str):
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Administration rights required"}), 403
    user = User.query.get(user_id)
    if not user:
        abort(404, f"User with ID {user_id} not found")
    db.session.delete(user)
    db.session.commit()
    return "", 204
