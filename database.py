import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, login_required, logout_user
from flask_bootstrap import Bootstrap


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Connects our Flask App to our Database

app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)

login_manager = LoginManager()
login_manager.init_app(app)

Bootstrap(app)