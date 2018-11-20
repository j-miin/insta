from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from database import db,app
from model import User
from form import RegistrationForm


@app.route("/")
def index():	
	return render_template('index.html')

@app.route("/instagram/signup", methods=['GET', 'POST'])
def new():
	return render_template('signup.html')

@app.route("/instagram/users", methods=["POST"])
def create():		
	username = request.form.get('username')
	email = request.form.get('email')
	password = request.form.get('password')	
	new_user = User(username, email, password)
	new_user.set_password(password)
	db.session.add(new_user)
	db.session.commit()		
	user = User.query.get(new_user.id)
	return render_template('show.html', user=user)

@app.route("/instagram/userlist", methods=["GET"])
def base():
	all_user = User.query.all()
	return render_template('base.html', all_user=all_user)

@app.route("/instagram/users/<id>", methods=["POST"])
def update_or_delete(id):
	if request.form.get('_method') == "PUT":
		new_username = request.form.get('name')
		new_email = request.form.get('email')
		new_password = request.form.get('password')	
		edit_user=User(new_username, new_email, new_password)
		edit_user.set_password(new_password)
		db.session.add(edit_user)
		db.session.commit()
		user = User.query.get(id)	
		return redirect(f"/instagram/users/{id}")

	elif request.form.get('_method') == "DELETE":
		user = User.query.get(id)
		db.session.delete(user)
		db.session.commit()
		return redirect('/instagram/userlist')

if __name__ == '__main__':
	app.run()	
	

