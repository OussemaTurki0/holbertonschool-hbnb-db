from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.place import Place
from models.country import Country
from models.city import City
from models.amenity import Amenity
import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.base_model import BaseModel

# Your test code here

# Configure test database connection
DATABASE_URL = "sqlite:///test_database.db"
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Create tables
def create_tables():
    Base.metadata.create_all(engine)
    print("Tables created")

# Function to add a user
def add_user(first_name, last_name, email, password, is_admin=False):
    new_user = User(first_name=first_name, last_name=last_name, email=email, password=password, is_admin=is_admin)
    session.add(new_user)
    session.commit()
    print("User added successfully")

# Function to read a user
def get_user(email):
    user = session.query(User).filter_by(email=email).first()
    return user

# Function to update a user
def update_user(email, first_name=None, last_name=None, password=None, is_admin=None):
    user = session.query(User).filter_by(email=email).first()
    if user:
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if password:
            user.password = password
        if is_admin is not None:
            user.is_admin = is_admin
        session.commit()
        print("User updated successfully")
    else:
        print("User not found")

# Function to delete a user
def delete_user(email):
    user = session.query(User).filter_by(email=email).first()
    if user:
        session.delete(user)
        session.commit()
        print("User deleted successfully")
    else:
        print("User not found")

if __name__ == "__main__":
    create_tables()

    # Add a user
    add_user("John", "Doe", "john.doe@example.com", "password123")

    # Get the added user
    user = get_user("john.doe@example.com")
    print(user.to_dict() if user else "User not found")

    # Update the user
    update_user("john.doe@example.com", first_name="Jonathan")

    # Get the updated user
    user = get_user("john.doe@example.com")
    print(user.to_dict() if user else "User not found")

    # Delete the user
    delete_user("john.doe@example.com")

    # Try to get the deleted user
    user = get_user("john.doe@example.com")
    print(user.to_dict() if user else "User not found")
