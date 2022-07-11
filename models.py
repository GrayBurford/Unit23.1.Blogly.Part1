"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User (db.Model):
    """Create a new user."""

    __tablename__ = "blogly"

    id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement = True
    )
    first_name = db.Column(
        db.String(20),
        nullable = False
    )
    last_name = db.Column(
        db.String(30),
        nullable = False
    )
    image_url = db.Column(
        db.String,
        nullable = False,
        default="https://image.shutterstock.com/image-vector/anonymous-vector-icon-incognito-sign-260nw-1850222983.jpg"
    )

    def get_full_name(self):
        """Returns full name"""

        return f"{self.first_name} {self.last_name}"

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)