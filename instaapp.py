from flask import render_template, request, redirect, url_for, flash
from database import db,app, login_manager
from model import User
from form import RegistrationForm, LoginForm
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from werkzeug.security import check_password_hash

@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(user_id)
    except:
        return None

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/instagram/signup", methods=['GET', 'POST'])
def new():
    form=RegistrationForm()    
    return render_template('register.html', form=form)


@app.route("/instagram/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("You're logged in")
        return redirect(url_for('index'))
    form=LoginForm()
    return render_template('login.html', form=form)

    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('login.html', form=form)

@app.route("/instagram/users", methods=["POST"])
def create():	
	form = RegistrationForm(request.form)	
	new_user = User(form.username.data, form.email.data, form.password.data)
	new_user.set_password(form.password.data)
	if new_user.validation_errors == []: 
		db.session.add(new_user)
		db.session.commit()	
		return redirect(url_for('login'))
	
	return render_template('register.html', form=form, validation_errors=new_user.validation_errors)

@app.route("/instagram/userlist", methods=["GET"])
def base():
	all_user = User.query.all()
	return render_template('base.html', all_user=all_user)

@app.route("/instagram/users", methods=["POST"])
def update_or_delete():
	# form = EditForm(request.form)
	if request.form.get('_method') == "PUT":		 
		edit_user = User(form.username.data, form.email.data, form.password.data)
		edit_user.set_password(new_password)
		db.session.add(edit_user)
		db.session.commit()		
		return redirect('/instagram/userlist')

	elif request.form.get('_method') == "DELETE":
		user = User.query.get(id)
		db.session.delete(user)
		db.session.commit()
		return redirect('/instagram/userlist')

if __name__ == '__main__':
	app.run()	
	

