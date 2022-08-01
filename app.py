"""Blogly application."""

from flask import Flask, request, render_template, redirect
from models import db, connect_db, User, Post
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

@app.route('/users/<int:user_id>', methods=['GET', 'POST'])
def show_user_details(user_id):
    """Display a single user's details"""

    user = User.query.get_or_404(user_id)
    posts = Post.query.all()
    return render_template("details.html", user=user, posts=posts)

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

######### POSTS ########

@app.route('/users/<int:user_id>/posts/new')
def create_new_post(user_id):
    """Show form for user to create new post."""

    user = User.query.get_or_404(user_id)
    return render_template('new_post_form.html', user=user)

@app.route('/users/<int:user_id>/posts/new', methods=["POST"])
def handle_new_post(user_id):
    """Handle form submission to create new post."""

    user = User.query.get_or_404(user_id)
    new_title = request.form['title']
    new_body = request.form['text']
    new_post = Post(title=new_title, content=new_body, user_id=user.id)

    db.session.add(new_post)
    db.session.commit()

    return redirect(f"/users/{user_id}")

@app.route("/posts/<int:post_id>")
def show_posts(post_id):
    """Display a specific post page."""

    post = Post.query.get_or_404(post_id)

    return render_template('show_post.html', post=post)

@app.route("/posts/<int:post_id>/edit")
def show_post_edit(post_id):
    """Display edit form for a specific user's post"""

    post = Post.query.get_or_404(post_id)
    return render_template('edit_post.html', post=post)

@app.route("/posts/<int:post_id>/edit", methods=['POST'])
def handle_post_eddit(post_id):
    """Handle form submission for editing a user's post"""

    post = Post.query.get_or_404(post_id)
    post.title = request.form['title']
    post.content = request.form['content']

    db.session.add(post)
    db.session.commit()

    return redirect(f"/users/{post.user_id}")

@app.route("/posts/<int:post_id>/delete", methods=['POST'])
def delete_post(post_id):
    """Handle button submit for deleting a post"""

    post = Post.query.get_or_404(post_id)
    
    db.session.delete(post)
    db.session.commit()

    return redirect(f"/users/{post.user_id}")