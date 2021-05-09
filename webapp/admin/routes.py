from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_required
from webapp.admin import bp
from webapp.admin.forms import JobForm, CompanyForm, PostForm
from webapp.models import Job, Company, Post

@bp.route('/admin')
def admin():
	return render_template('admin/admin.html')


@bp.route('/jobs')
@login_required
def jobs():
	my_jobs = current_user.jobs
	return render_template('admin/jobs.html', jobs=my_jobs)

@bp.route('/add_job', methods=['GET', 'POST'])
@login_required
def add_job():
	form = JobForm()

	if request.method == 'POST':
		if form.validate_on_submit:
			job = Job()
			company = Company.objects(name=form.company.data).first()
			job.company = company
			job.start_date = form.start_date.data
			job.end_date = form.end_date.data
			job.job_title = form.job_title.data
			job.description = form.description.data
			job.achievements = form.achievements.data
			current_user.add_job(job)
			current_user.save()
			return redirect(url_for('admin.jobs'))
	
	return render_template('admin/add_job.html', form=form)

@bp.route('/remove_job', methods=['POST'])
@login_required
def remove_job():
	job_id = request.args.get('job_id')
	print(job_id)
	job = [job for job in current_user.jobs if str(job.oid) == str(job_id)]
	print(job[0].oid)
	current_user.remove_job(job[0])
	current_user.save()
	return redirect(url_for('admin.jobs'))

@bp.route('/edit_job/<job_id>', methods=['GET', 'POST'])
@login_required
def edit_job(job_id):
	job_list = [job for job in current_user.jobs if str(job.oid) == str(job_id)]
	job = job_list[0]
	form = JobForm()
	if request.method == 'POST':
		if form.validate_on_submit:
			company = Company.objects(name=form.company.data).first()
			job.company = company
			job.start_date = form.start_date.data
			job.end_date = form.end_date.data
			job.job_title = form.job_title.data
			job.description = form.description.data
			job.achievements = form.achievements.data
			current_user.save()
			return redirect(url_for('admin.jobs'))

	form.company.data = job.company
	form.job_title.data = job.job_title
	form.start_date.data = job.start_date
	form.end_date.data = job.end_date
	form.description.data = job.description
	form.achievements.data = job.achievements

	return render_template('admin/edit_job.html', form=form, job=job)

@bp.route('/add_company', methods=['GET', 'POST'])
@login_required
def add_company():
	form = CompanyForm()

	if request.method == 'POST':
		if form.validate_on_submit:
			company = Company()
			company.name = form.name.data
			company.description = form.description.data
			company.img_url = form.img_url.data
			company.save()
			return redirect(url_for('admin.jobs'))
	
	return render_template('admin/add_company.html', form=form)

@bp.route('/posts', methods=['GET', 'POST'])
@login_required
def posts():
	posts = current_user.posts
	return render_template('admin/posts.html', posts=posts)

@bp.route('/new_blog_post', methods=['GET', 'POST'])
@login_required
def new_blog_post():
	form = PostForm()
	if form.validate_on_submit():
		post = Post()
		post.title = form.title.data
		post.body = form.body.data
		current_user.post(post)
		current_user.save()
		return redirect(url_for('admin.posts'))
	return render_template('admin/new_blog_post.html', form=form)

@bp.route('/edit_blog_post/<post_oid>', methods=['GET', 'POST'])
@login_required
def edit_blog_post(post_oid):
	bp = [post for post in current_user.posts if str(post_oid) == str(post.oid)][0]
	form = PostForm()

	if form.validate_on_submit():
		bp.title = form.title.data
		bp.body = form.body.data
		current_user.save()
		return redirect(url_for('admin.posts'))

	form.title.data = bp.title
	form.body.data = bp.body

	return render_template('admin/edit_post.html', form=form, post=bp)

@bp.route('/remove_post', methods=['POST'])
@login_required
def remove_post():
	post_id = request.args.get('post_id')
	p = [post for post in current_user.posts if str(post.oid) == str(post_id)][0]
	current_user.remove_post(p)
	current_user.save()
	return redirect(url_for('admin.posts'))



