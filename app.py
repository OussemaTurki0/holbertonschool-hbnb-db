from flask import Flask, jsonify, request
from models.base_model import BaseModel
from data_manager import get_session
from models.user import User
from models.review import Review
from models.place import Place
from models.country import Country
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)
app.secret_key = "secret key"
db = SQLAlchemy(app)