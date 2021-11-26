from search import app
from search.forms import RegisterForm, LoginForm
from flask import render_template, redirect, url_for, flash, request
from search.models import User
from search import db

# route decorater
@app.route('/')
@app.route('/home')
def home_page():
	return render_template('home.html')

@app.route('/upload')
def upload():
	return render_template('upload.html')

@app.route('/login', methods=['GET', 'POST'])
def login_page():
	form = LoginForm()
	if form.validate_on_submit():
		attempted_user = User.query.filter_by(username=form.username.data).first()
		if attempted_user and attempted_user.password_hash == form.password.data:
			# login_user(attempted_user)
			flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
			return redirect(url_for('upload'))
		else:
			flash('Username and/or password did not match! Please try again later', category='danger')

	return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
	form = RegisterForm()
	if form.validate_on_submit():
		new_user = User(username=form.username.data,
			email_address=form.email_address.data,
			password_hash=form.password1.data)
		db.session.add(new_user)
		db.session.commit()
		flash(f'Account created successfully!', category="success")

	if form.errors != {}:
		for err_msg in form.errors.values():
			flash(f'There was error creating user {err_msg}', category="danger")
	return render_template('register.html', form=form)