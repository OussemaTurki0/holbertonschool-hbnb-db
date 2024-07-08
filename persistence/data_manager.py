import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import User
from models.base_model import Base
from persistence.ipersistence_manager import IPersistenceManager

# Configure database connection
class DataManager(IPersistenceManager):
    def __init__(self):
        self.use_database = os.getenv('USE_DATABASE', 'True').lower() == 'true'
        DATABASE_URL = "sqlite:///test_database.db"
        self.engine = create_engine(DATABASE_URL, echo=True)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    # Create tables
    def create_tables(self):
        Base.metadata.create_all(self.engine)
        print("Tables created")

    # Concrete implementation of abstract methods

    def save(self, entity):
        self.session.add(entity)
        self.session.commit()

    def get(self, entity_id):
        return self.session.query(User).get(entity_id)

    def update(self, entity_id, data):
        entity = self.session.query(User).get(entity_id)
        if entity:
            for key, value in data.items():
                setattr(entity, key, value)
            self.session.commit()
        return entity

    def delete(self, entity_id):
        entity = self.session.query(User).get(entity_id)
        if entity:
            self.session.delete(entity)
            self.session.commit()

    def get_all(self):
        return self.session.query(User).all()

    def close_session(self):
        self.session.close()
