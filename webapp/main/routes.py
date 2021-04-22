from flask import current_app, render_template, url_for, redirect, flash, jsonify, request
from webapp.models import User
from webapp.main import bp
from wordcloud import WordCloud
import base64
import io
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
	soft_skills = 'stakeholder management, presenting, written communication, verbal communication'
	hard_skills = 'discovery, delivery, story mapping, user testing, AB testing'

	def get_wordcloud(text, colormap):
		pil_img = WordCloud(height=400, random_state=1, background_color='navy', colormap=colormap).generate(text=text).to_image()
		img = io.BytesIO()
		pil_img.save(img, "PNG")
		img.seek(0)
		img_b64 = base64.b64encode(img.getvalue()).decode()
		return img_b64

	
	
	soft_skills_cloud = get_wordcloud(soft_skills, 'rainbow')
	hard_skills_cloud = get_wordcloud(hard_skills, 'magma_r')

	return render_template('main/skills.html', title='Skills', soft_skills_cloud=soft_skills_cloud, hard_skills_cloud=hard_skills_cloud)

@bp.route('/tools')
def tools():
	return render_template('main/tools.html', title='Tools')

@bp.route('/personal')
def personal():
	return render_template('main/personal.html', title='Away From Work')

@bp.route('/blog')
def blog():
	return render_template('main/blog.html', title='Blog')







