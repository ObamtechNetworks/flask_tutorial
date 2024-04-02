from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# create a Flask instance
app = Flask(__name__)
# set a secret key
app.config['SECRET_KEY'] = 'd6bb5a45fdc0aad533297f7cc88980cb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# create a database instance
db = SQLAlchemy(app)
# for password hashing
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # the route function, this locates it
login_manager.login_message_category = 'info'  # for bootstrap when a user login


# import routes after initizlation
from flaskblog import routes