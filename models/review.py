from flask_sqlalchemy import SQLAlchemy

SQL = SQLAlchemy()

class Review(SQL.Model):
    """Review representation"""

    __tablename__ = 'reviews'

    id = SQL.Column(SQL.String(36), primary_key=True)
    place_id = SQL.Column(SQL.String(36), SQL.ForeignKey('places.id'), nullable=False)
    user_id = SQL.Column(SQL.String(36), SQL.ForeignKey('users.id'), nullable=False)
    comment = SQL.Column(SQL.Text, nullable=False)
    rating = SQL.Column(SQL.Float, nullable=False)
    created_at = SQL.Column(SQL.DateTime, default=SQL.func.current_timestamp())
    updated_at = SQL.Column(SQL.DateTime, onupdate=SQL.func.current_timestamp())
    place = SQL.relationship('Place', back_populates='reviews')
    user = SQL.relationship('User', back_populates='reviews')

    def __init__(self, place_id: str, user_id: str, comment: str, rating: float):
        self.place_id = place_id
        self.user_id = user_id
        self.comment = comment
        self.rating = rating

    def __repr__(self) -> str:
        """String representation of the object"""
        return f"<Review {self.id} - '{self.comment[:25]}...'>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "place_id": self.place_id,
            "user_id": self.user_id,
            "comment": self.comment,
            "rating": self.rating,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @staticmethod
    def create(data: dict) -> "Review":
        """Create a new review"""
        from models.user import User
        from models.place import Place
        user = User.query.get(data["user_id"])
        if not user:
            raise ValueError(f"User with ID {data['user_id']} not found")
        place = Place.query.get(data["place_id"])
        if not place:
            raise ValueError(f"Place with ID {data['place_id']} not found")
        new_review = Review(
            place_id=data["place_id"],
            user_id=data["user_id"],
            comment=data["comment"],
            rating=float(data["rating"])
        )
        SQL.session.add(new_review)
        SQL.session.commit()
        return new_review

    @staticmethod
    def update(review_id: str, data: dict) -> "Review | None":
        """Update an existing review"""
        review = Review.query.get(review_id)
        if not review:
            raise ValueError("Review not found")
        for key, value in data.items():
            setattr(review, key, value)
        SQL.session.commit()
        return review
