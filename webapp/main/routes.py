from flask import current_app, render_template, url_for, redirect, flash, jsonify, request
from flask_login import current_user, login_user, logout_user, login_required
from webapp.models import User
from webapp.main import bp

@bp.route('/')
@bp.route('/index')
def index():
	return render_template('main/index.html', title='Home')

@bp.route('/career')
def career():
	return render_template('main/career.html', title='Career Journey')

@bp.route('/skills')
def skills():
	return render_template('main/skills.html', title='Skills')

@bp.route('/tools')
def tools():
	return render_template('main/tools.html', title='Tools')

@bp.route('/personal')
def personal():
	return render_template('main/personal.html', title='Away From Work')

@bp.route('/blog')
def blog():
	return render_template('main/blog.html', title='Blog')







