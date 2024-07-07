""" run the app"""

from flask import Flask
from flask_jwt_extended import JWTManager
from routes import register_routes
from flask_sqlalchemy import SQLAlchemy
from requests.__init__ import create_app, db, jwt, bcryptgit

# Initialize the Flask application using create_app() from __init__.py
app = create_app()

# App configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'Holberton123456'

db = SQLAlchemy(app)

# Register all routes using the register_routes function
register_routes(app)

# Create tables based on models
db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
