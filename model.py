import re
from sqlalchemy.orm import validates
from database import db, login_manager
from helpers import validation_preparation
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(user_id)
    except:
        return None

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    email = db.Column(db.Text)
    password = db.Column(db.Text)

    def __init__(self,username,email,password):
        self.username = username
        self.email = email       
        self.password = password

    def __repr__(self):
        return f"User {self.username} is registered."

    @validates('username')
    @validation_preparation
    def validate_username(self, key, username):
        if not username:
            self.validation_errors.append('No username provided')

        if (not self.username == username):
            if User.query.filter_by(username=username).first():
                self.validation_errors.append('Username is already in use')

        if len(username) < 5 or len(username) > 20:
            self.validation_errors.append(
                'Username must be between 5 and 20 characters')

        return username

    @validates('email')
    @validation_preparation
    def validate_email(self, key, email):
        if not email:
            self.validation_errors.append('No email provided')

        if not re.match("[^@]+@[^@]+\\.[^@]+", email):
            self.validation_errors.append(
                'Provided email is not an email address')

        if (not self.email == email):
            if User.query.filter_by(email=email).first():
                self.validation_errors.append('Email is already in use')

        return email

    @validation_preparation
    def set_password(self, key, password):
        if not password:
            self.validation_errors.append('Password not provided')

        if len(password) < 8 or len(password) > 50:
            self.validation_errors.append('Password must be between 8 and 50 characters')

        self.password_hash = generate_password_hash(password)

        return password_hash

