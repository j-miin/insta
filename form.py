from flask_wtf import FlaskForm
from wtforms import TextField, StringField, SubmitField, PasswordField
from werkzeug.security import check_password_hash

class RegistrationForm(FlaskForm):
	username = StringField('username')
	email = StringField('email')
	password = PasswordField('password')
	submit = SubmitField("Sign In")
	

