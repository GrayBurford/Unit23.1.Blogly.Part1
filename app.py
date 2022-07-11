"""Blogly application."""

from multiprocessing.reduction import sendfds
from flask import Flask, request, render_template, redirect
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "SHHHH!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """Home Page. Redirects to list of users."""

    return redirect('/users')

@app.route('/users')
def all_users():
    """List of all users page."""

    all_users = User.query.all()

    return render_template('users.html', all_users=all_users)

@app.route('/users/new', methods=['GET'])
def create_user():
    """Create new user form page."""

    return render_template('new_user.html')


@app.route('/users/new', methods=['POST'])
def create_user_submition():
    """Submit form for creating new user."""

    f = request.form['f_name']
    l = request.form['l_name']
    i = request.form['image_url']

    new_user = User(first_name = f, last_name = l, image_url = i)

    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>', methods=['GET'])
def show_user_details(user_id):
    """Display a single user's details"""

    user = User.query.get_or_404(user_id)
    return render_template("details.html", user=user)

@app.route('/users/<int:user_id>/edit', methods=['GET'])
def edit_page(user_id):
    """Show form to edit user's page."""

    user = User.query.get_or_404(user_id)
    return render_template('edit.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=["POST"])
def confirm_user_edit(user_id):
    """Handle form submssion and update user info."""

    user = User.query.get_or_404(user_id)    
    user.first_name = request.form['f_name']
    user.last_name = request.form['l_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect("/")

@app.route('/users/<int:user_id>/delete', methods=['GET'])
def delete_user(user_id):
    """Process form submission to delete user."""

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect('/users')

# MAKE ROUTES FOR THE FOLLOWING:

# 1. GET /
# Redirect to list of users. (We’ll fix this in a later step).

# 2. GET /users
# Show all users.
# Make these links to view the detail page for the user.
# Have a link here to the add-user form.

# 3. GET /users/new
# Show an add form for users.

# 4. POST /users/new
# Process the add form, adding a new user and going back to /users

# 5. GET /users/[user-id]
# Show information about the given user.
# Have a button to get to their edit page, and to delete the user.

# 6. GET /users/[user-id]/edit
# Show the edit page for a user.
# Have a cancel button that returns to the detail page for a user, and a save button that updates the user.

# 7. POST /users/[user-id]/edit
# Process the edit form, returning the user to the /users page.

# 8. POST /users/[user-id]/delete
# Delete the user.