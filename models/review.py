from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey, Text, Relationship

class Review(Base):
    __tablename__ = 'reviews'

	id = Column(Integer, primary_key=True, autoincrement=True)
	user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
	place_id = Column(Integer, ForeignKey('places.id', nullable=False))
	rating = Column(Integer, nullable=False)
	text = Column(Integer, nullable=False)
    user = relationship('User', back_populates='reviews')

	def __init__(self, user_id, place_id, rating, text):
        super().__init__()
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.text = text