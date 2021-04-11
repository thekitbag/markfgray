from flask import current_app, render_template, url_for, redirect, flash, jsonify, request
from webapp.models import User
from webapp.main import bp
import config 

@bp.route('/')
@bp.route('/index')
def index():
	return render_template('main/index.html', title='Home')

@bp.route('/career')
def career():
	username = current_app.config['USERNAME']
	user = User.objects(username=username).first()
	jobs = user.jobs
	jobs.sort(key=lambda x: x.start_date, reverse=True)
	return render_template('main/career.html', title='Career Journey', jobs=jobs)

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







