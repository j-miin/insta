from database import db
from werkzeug.security import generate_password_hash

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    email = db.Column(db.Integer)
    password = db.Column(db.Text)

    def __init__(self,name,age,breed):
        self.username = username
        self.email = email
        self.set_password(password)

    def set_password(self, password):
    	self.hash_password = generate_password_hash(password)
