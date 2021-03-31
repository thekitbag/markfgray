from flask import render_template
from flask_login import current_user, login_required
from webapp.admin import bp

@bp.route('/admin')
def admin():
	return render_template('admin.html')

@bp.route('/new_blog_post', methods=['GET', 'POST'])
@login_required
def new_blog_post():
	return render_template('new_blog_post.html')