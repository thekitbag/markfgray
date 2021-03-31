from flask import render_template
from webapp.auth import bp
from webapp.auth.forms import RegistrationForm, LoginForm

@bp.route('/admin')
def admin():
	return render_template('admin.html', title='Admin')

@bp.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()

	if form.validate_on_submit():
		user = User(username=form.username.data.lower())
		user.set_password(form.password.data)
		user.save()
		return jsonify(user.to_json())
	else:
		return render_template('register.html', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		username = form.username.data.lower()
		user = User.objects(username=username).first()

		if user is None or not user.check_password(form.password.data):
			flash('Invalid login details')
			return redirect(url_for('admin.login'))
		login_user(user)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('main.index')
		return redirect(next_page)
	else:
		return render_template('login.html', form=form)

@bp.route('/logout', methods=['GET'])
def logout():
	logout_user()
	return redirect(url_for('main.index'))