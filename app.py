""" run the app"""

from flask import Flask
from flask_jwt_extended import JWTManager
from models import db, bcrypt
from controolers import user

app = Flask(__name__)

# Configuration de l'application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///***********.*****'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'Holberton123456'

# Initialisation des extensions
SQL.init_app(app)
bcrypt.init_app(app)
jwt = JWTManager(app)

# Routes de votre application
app.add_url_rule('/users', 'get_users', user.get_users, methods=['GET'])
app.add_url_rule('/users', 'create_user', user.create_user, methods=['POST'])
app.add_url_rule('/users/<user_id>', 'get_user_by_id', user.get_user_by_id, methods=['GET'])
app.add_url_rule('/users/<user_id>', 'update_user', user.update_user, methods=['PUT'])
app.add_url_rule('/users/<user_id>', 'delete_user', user.delete_user, methods=['DELETE'])

app = create_app()

if __name__ == "__main__":
    app.run(debug=False)