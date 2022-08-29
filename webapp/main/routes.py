from flask import current_app, render_template, url_for, redirect, flash, jsonify, request
from webapp.models import User
from webapp.main import bp
from webapp.main.blog_post_formatter import BlogPost
from wordcloud import WordCloud
import base64
import io
import config
from datetime import datetime

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
	today = datetime.today()
	return render_template('main/career.html', title='Career Journey', jobs=jobs, today=today)

@bp.route('/skills')
def skills():
	skills = 'stakeholder management, presenting, written communication, verbal communication, discovery, delivery, story mapping, \
			user testing, AB_testing, customer interviews, product strategy, vision, opportunity/solution tree, assumptions mapping,\
			HTML, CSS, JavaScript, Python, SQL, Git, web analytics, Scrum, Kanban, VMOST, Agile, OKRs, CSPO, Northstar'

	def get_wordcloud(text, colormap):
		pil_img = WordCloud(height=600, width=1000, random_state=1, colormap=colormap).generate(text=text).to_image()
		img = io.BytesIO()
		pil_img.save(img, "PNG")
		img.seek(0)
		img_b64 = base64.b64encode(img.getvalue()).decode()
		return img_b64



	skills_cloud = get_wordcloud(skills, 'BuPu_r')

	return render_template('main/skills.html', title='Skills', skills_cloud=skills_cloud)

@bp.route('/tools')
def tools():
	return render_template('main/tools.html', title='Tools')

@bp.route('/personal')
def personal():
	return render_template('main/personal.html', title='Away From Work')

@bp.route('/blog')
def blog():
	username = current_app.config['USERNAME']
	user = User.objects(username=username).first()
	posts = user.posts
	print(posts)
	posts.sort(key=lambda x: x.post_date, reverse=True)
	return render_template('main/blog.html', title='Blog', posts=posts)

@bp.route('/post/<post_id>')
def post(post_id):
	username = current_app.config['USERNAME']
	user = User.objects(username=username).first()
	post_object = [i for i in user.posts if str(i.oid) == str(post_id)][0]
	blogpost = BlogPost(post_object)
	return render_template('main/blog_post.html', blogpost=blogpost)
