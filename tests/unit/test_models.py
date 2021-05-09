from webapp.models import User, Job, Company, Post
from werkzeug.security import generate_password_hash
from datetime import datetime

def test_new_user(new_user):
	"""
	GIVEN a User model
	WHEN a new User is created
	THEN check the the username and pwd_hash role fields are defined correctly
	"""

	assert new_user.username == 'freddy function user'
	assert new_user.pwd_hash != 'password1'
	assert new_user.check_password('password99') == False
	assert new_user.check_password('password1') == True
	assert type(new_user.to_json()) == dict

def test_new_job(new_user):
	"""
	GIVEN a user
	WHEN a new job is created and added to that user model
	THEN the fields in that job should be created correctly and accessible through the users jobs field
	"""
	job = Job()
	job.company = 'Google'
	job.start_date = datetime(1970, 1, 1, 0, 0 ,0)
	job.end_date = datetime(1987, 5, 5, 5, 5, 5, 5)
	job.job_title = 'CEO'
	job.description = "As CEO I dominated the industry, growing revenue by 100% every year and scaling \
					the company to 100,000 employees"
	new_user.jobs.append(job)

	assert new_user.jobs == [job]
	assert new_user.jobs[0].company == 'Google'
	assert new_user.jobs[0].start_date == datetime(1970, 1, 1, 0, 0 ,0)
	assert new_user.jobs[0].end_date == datetime(1987, 5, 5, 5, 5, 5, 5)
	assert new_user.jobs[0].job_title == 'CEO'
	assert new_user.jobs[0].description == "As CEO I dominated the industry, growing revenue by 100% every year and scaling \
					the company to 100,000 employees"

def test_add_job(new_user):
	"""
	GIVEN a user and a job
	WHEN the add job method is called for that job
	THEN the job is in the users jobs attribute
	"""
	j = Job()
	new_user.add_job(j)
	assert j in new_user.jobs
	assert j.oid == new_user.jobs[0].oid

def test_add_two_jobs(new_user):
	"""
	GIVEN a user
	WHEN that user adds two jobs
	THEN both jobs should appear in the users jobs attribute and both jobs IDs should be unique
	"""
	j = Job()
	new_user.add_job(j)
	j2 = Job()
	new_user.add_job(j2)
	assert j in new_user.jobs
	assert j2 in new_user.jobs
	assert j.oid == new_user.jobs[0].oid
	assert j2.oid == new_user.jobs[1].oid
	assert j.oid != j2.oid

def test_remove_job(user_with_job):
	"""
	GIVEN a user with a job
	WHEN the remove job method is called for that job
	THEN that job should no longer be in the user's jobs
	"""
	assert len(user_with_job.jobs) == 1
	job = user_with_job.jobs[0]
	user_with_job.remove_job(job)
	assert len(user_with_job.jobs) == 0

def test_new_job_new_company(new_user):
	"""
	GIVEN a user
	WHEN user adds a new job at a new company
	THEN that jobs should appear in user's jobs
	"""
	j = Job()
	c = Company()
	c.name = 'Facebook'
	j.company = c
	new_user.add_job(j)
	assert new_user.jobs[0].company.name == 'Facebook'

def test_new_blog_post(new_user):
	"""
	GIVEN a user
	WHEN that user makes a new post
	THEN post should appear un user's posts
	"""
	assert new_user.posts == []
	p = Post()
	p.title = 'Hello World'
	p.body = 'This is my first blog post, I can\'t wait to start talking to the world about myself'
	new_user.post(p)
	assert new_user.posts == [p]









						