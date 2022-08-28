import os
from flask import render_template, request, url_for, redirect, flash, jsonify
from flask_login import current_user, login_user, logout_user
from webapp.models import User
from webapp.auth import bp
from webapp.auth.forms import RegistrationForm, LoginForm

@bp.route('/admin')
def admin():
	return render_template('auth/admin.html', title='Admin')

@bp.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		if form.secret_number.data != os.environ.get('SECRET_NUMBER'):
			return redirect(url_for('main.index'))
		username = form.username.data.lower()
		user = User.objects(username=username).first()

		if user is None or not user.check_password(form.password.data):
			flash('Invalid login details')
			return redirect(url_for('auth.login'))
		login_user(user)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('admin.admin')
		return redirect(next_page)
	else:
		return render_template('auth/login.html', form=form)

@bp.route('/logout', methods=['GET'])
def logout():
	logout_user()
	return redirect(url_for('main.index'))
