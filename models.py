"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

default_img = "https://image.shutterstock.com/image-vector/anonymous-vector-icon-incognito-sign-260nw-1850222983.jpg"

class User(db.Model):
    """Create a new user."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    first_name = db.Column(db.String(20), nullable = False)
    last_name = db.Column(db.String(30), nullable = False)
    image_url = db.Column(db.Text, nullable = False, default=default_img)

    posts = db.relationship('Post', cascade="all, delete-orphan") 
    # OR: posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User: {self.id} -- {self.first_name} -- {self.last_name} -- {self.image_url}>"

    def get_full_name(self):
        """Returns full name"""

        return f"{self.first_name} {self.last_name}"

class Post(db.Model):
    """Create new blog posts"""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(80), unique=True, nullable = False)
    content = db.Column(db.Text, nullable = False)
    created_at = db.Column(db.DateTime, nullable = False, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)

    users = db.relationship('User') 

    def __repr__(self):
        return f"<Post: {self.id} -- {self.title} -- {self.content} -- {self.created_at} -- {self.user_id}>"

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)