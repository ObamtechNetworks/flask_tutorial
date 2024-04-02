from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

# create a registration form class and inherit from FlaskForm
class RegistrationForm(FlaskForm):
    """To handle registration forms"""
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                            validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # validators for username and email field
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')
    

        # validators for the email field
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    """To handle login"""
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                            validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    """To handle registration forms"""
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    # to handle changing of picture, FileAllowed allows a list of allowed extensions
    # ensure this is rendered on our template
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    # validators for username and email field
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

        # validators for the email field
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

# create a post form
class PostForm(FlaskForm):
    """Handles the creation of new posts"""
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')