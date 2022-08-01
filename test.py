from unittest import TestCase
from models import db, User, Post
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///testing_db'
app.config['SQLALCHEMY_ECHO'] = False

# To execute tests: python -m unittest NAME_OF_FILE (runs all cases)

# assertEqual(a, b); a == b
# assertNotEqual(a, b); a != b
# assertTrue(x); bool(x) is True
# assertFalse(x); bool(x) is False
# assertIs(a, b); a is b
# assertIsNot(a, b); a is not b
# assertIsNone(x); x is None
# assertIsNotNone(x); x is not None
# assertIn(a, b); a in b
# assertNotIn(a, b); a not in b
# assertIsInstance(a, b); isinstance(a, b)
# assertNotIsInstance(a, b); not isinstance(a, b)

class TestingBlogly (TestCase):
    """Unit Tests for Blogly app"""

    def setUp(self):
        """Actions to take before running each function test"""

        # User.query.delete()
        # Post.query.delete()
        db.drop_all()
        db.create_all()
    
    def tearDown(self):
        """Actions to take after each unittest runs."""

        db.session.rollback()

    # Unit tests must start with test_
    def test_user_id(self):
        new_user = User(first_name='abc', last_name='zyx')
        db.session.add(new_user)
        db.session.commit()
        self.assertEqual(new_user.id, 1)

    def test_first_name(self):
        new_user = User(first_name='abc', last_name='zyx')
        db.session.add(new_user)
        db.session.commit()
        self.assertEqual(new_user.first_name, 'abc')

    def test_last_name(self):
        new_user = User(first_name='abc', last_name='zyx')
        db.session.add(new_user)
        db.session.commit()
        self.assertEqual(new_user.last_name, 'zyx')

    def test_image_url(self):
        new_user = User(first_name='abc', last_name='zyx')
        db.session.add(new_user)
        db.session.commit()
        self.assertEqual(new_user.image_url, "https://image.shutterstock.com/image-vector/anonymous-vector-icon-incognito-sign-260nw-1850222983.jpg")

    def test_post_id(self):
        new_user = User(first_name='abc', last_name='zyx')
        db.session.add(new_user)
        db.session.commit()
        new_post = Post(title='Testing', content='Iamcontent', user_id=1)
        db.session.add(new_post)
        db.session.commit()
        self.assertEqual(new_post.id, 1)

    def test_post_title(self):
        new_user = User(first_name='abc', last_name='zyx')
        db.session.add(new_user)
        db.session.commit()
        new_post = Post(title='Testing', content='Iamcontent', user_id=1)
        db.session.add(new_post)
        db.session.commit()
        self.assertEqual(new_post.title, 'Testing')

    def test_post_content(self):
        new_user = User(first_name='abc', last_name='zyx')
        db.session.add(new_user)
        db.session.commit()
        new_post = Post(title='Testing', content='Iamcontent', user_id=1)
        db.session.add(new_post)
        db.session.commit()
        self.assertEqual(new_post.content, 'Iamcontent')

    def test_post_user_id(self):
        new_user = User(first_name='abc', last_name='zyx')
        db.session.add(new_user)
        db.session.commit()
        new_post = Post(title='Testing', content='Iamcontent', user_id=1)
        db.session.add(new_post)
        db.session.commit()
        self.assertEqual(new_post.user_id, 1)

    def test_home_route(self):
        with app.test_client() as client:
            response = client.get("/")
            self.assertEqual(response.status_code, 302)
            redirect_response = client.get("/users")
            self.assertEqual(redirect_response.status_code, 200)

    def test_user_profile(self):
        with app.test_client() as client:
            new_user = User(first_name='abc', last_name='zyx')
            db.session.add(new_user)
            db.session.commit()
            response = client.get(f"/users/{new_user.id}")
            self.assertEqual(response.status_code, 200)

    def test_delete_user(self):
        new_user = User(first_name='abc', last_name='zyx')
        db.session.add(new_user)
        db.session.commit()
        with app.test_client() as client:
            response = client.get(f'/users/{new_user.id}/delete')
            self.assertEqual(response.status_code, 302)
            all_users = User.query.all()
            self.assertEqual(len(all_users), 0)
