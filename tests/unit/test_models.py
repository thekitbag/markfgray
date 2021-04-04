from webapp.models import User, Job
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
	job.user = new_user
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
	



						