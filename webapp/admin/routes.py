from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_required
from webapp.admin import bp
from webapp.admin.forms import JobForm, CompanyForm
from webapp.models import Job, Company

@bp.route('/admin')
def admin():
	return render_template('admin/admin.html')

@bp.route('/new_blog_post', methods=['GET', 'POST'])
@login_required
def new_blog_post():
	return render_template('admin/new_blog_post.html')

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



