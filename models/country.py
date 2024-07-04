from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base_model import Base  # Adjust this as per your actual import structure

class Country(BaseModel):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    code = Column(String(3), nullable=False, unique=True)

    cities = relationship('City', back_populates='country', lazy=True)

    def __init__(self, name, code):
        super().__init__()
        self.name = name
        self.code = code

    def __repr__(self):
        """String representation of the object"""
        return f"<Country {self.code} ({self.name})>"

    def to_dict(self):
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @staticmethod
    def get_all():
        """Get all countries"""
        return Country.query.all()

    @staticmethod
    def get(code):
        """Get a country by its code"""
        return Country.query.filter_by(code=code).first()

    @staticmethod
    def create(name, code):
        """Create a new country"""
        new_country = Country(name=name, code=code)

        session.add(new_country)
        db.session.commit()

        return new_country
