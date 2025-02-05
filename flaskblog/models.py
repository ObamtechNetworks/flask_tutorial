from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # return the user for the given id


# create models
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')  # we're going to has them
    password = db.Column(db.String(60), nullable=False)
    # post attr has relationship with the Post model, use the author attr to get user who has the post
    # lazy=True, loads the data from the db in one go
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        """default representation for our class"""
        return f"User('{self.username}'), '{self.email}', '{self.image_file}')"


class Post(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    # This is the id of the user who authors the post
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        """default representation for our class"""
        return f"Post('{self.title}'), '{self.date_posted}')"