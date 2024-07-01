from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.user import User
from models.review import Review
from models.place import Place
from models.country import Country
from models.city import City
from models.amenity import Amenity

# Configure database connection
DATABASE_URL = "sqlite:///hbnb.db"  # Adjust this according to your database setup
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Create tables
def create_tables():
    Base.metadata.create_all(engine)
    print("Tables created")

# Function to add data (example)
def add_user(first_name, last_name, email, password, is_admin=False):
    new_user = User(first_name=first_name, last_name=last_name, email=email, password=password, is_admin=is_admin)
    session.add(new_user)
    session.commit()
    print("User added successfully")

# Additional functions for CRUD operations based on your project needs

if __name__ == "__main__":
    create_tables()  # Create tables when running data_manager.py
