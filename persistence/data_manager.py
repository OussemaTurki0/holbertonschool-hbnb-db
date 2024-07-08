from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import User
from models.review import Review
from models.place import Place
from models.country import Country
from models.city import City
from models.amenity import Amenity

# Configure database connection
class DataManager(IPersistenceManager):
    def __init__(self):
        self.use_database = os.getenv('USE_DATABASE', 'True').lower() == 'true'
        DATABASE_URL = "sqlite:///test_database.db"
        self.engine = create_engine(DATABASE_URL, echo=True)
        Self.Session = sessionmaker(bind=s/elf.engine)
        self.session = self.Session()

    # Create tables
    def create_tables(self):
        Base.metadata.create_all(self.engine)
        print("Tables created")

    # Function to add a user
    def add_user(self, first_name, last_name, email, password, is_admin=False):
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=password, is_admin=is_admin)
        self.session.add(new_user)
        self.session.commit()
        print("User added successfully")

    # Function to read a user
    def get_user(self, email):
        user = self.session.query(User).filter_by(email=email).first()
        return user

    # Function to update a user
    def update_user(self, email, first_name=None, last_name=None, password=None, is_admin=None):
        user = self.session.query(User).filter_by(email=email).first()
        if user:
            if first_name:
                user.first_name = first_name
            if last_name:
                user.last_name = last_name
            if password:
                user.password = password
            if is_admin is not None:
                user.is_admin = is_admin
            self.session.commit()
            print("User updated successfully")
        else:
            print("User not found")

    # Function to delete a user
    def delete_user(self, email):
        user = self.session.query(User).filter_by(email=email).first()
        if user:
            self.session.delete(user)
            self.session.commit()
            print("User deleted successfully")
        else:
            print("User not found")

    def close_session(self):
        self.session.close()