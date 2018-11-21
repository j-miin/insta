from flask_wtf import Form
from wtforms import TextField, StringField, SubmitField, PasswordField, BooleanField, validators

class RegistrationForm(Form):
	username = StringField('username')
	email = StringField('email')
	password = PasswordField('password')
	submit = SubmitField("Sign In")

class LoginForm(Form):
	username = StringField('username', validators=[validators.required()])	
	password = PasswordField('password', validators=[validators.required()])
	submit = SubmitField("Sign In")
	remember = BooleanField('remember_me')

class EditForm(Form):
	username = StringField('username')
	email = StringField('email')
	password = PasswordField('password')
	submit = SubmitField("Submit")

