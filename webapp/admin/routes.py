from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_required
from webapp.admin import bp
from webapp.admin.forms import JobForm
from webapp.models import Job

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
			job.company = form.company.data
			job.start_date = form.start_date.data
			job.end_date = form.end_date.data
			job.job_title = form.job_title.data
			job.description = form.description.data
			current_user.jobs.append(job)
			current_user.save()
			return redirect(url_for('admin.jobs'))
	
	return render_template('admin/add_job.html', form=form)