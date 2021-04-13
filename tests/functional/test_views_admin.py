from flask_login import current_user
from datetime import datetime
from flask import request, url_for

def test_new_blog_post_page(function_test_client, new_user):
	"""
	GIVEN a Flask application configured for testing AND I am not logged in
	WHEN I try to load the new blog post page
	THEN I should not be able to load the page
	"""
	with function_test_client as c:
		response = function_test_client.get('/new_blog_post')
		assert response.status_code == 401

		"""
		GIVEN a Flask application configured for testing AND I am logged in
		WHEN I try to load the new blog post page
		THEN I should be able to AND I should see the right content
		"""

		response_2 = function_test_client.post('/auth/login',
										data=dict(username='freddy function user', password='password1'), follow_redirects=True)
		response_3 = function_test_client.get('/new_blog_post')
		assert response_3.status_code == 200

def test_edit_jobs_page(function_test_client, logged_in_client):
	"""
	GIVEN a Flask application configured for testing AND I am not logged in
	WHEN I try to load the edit jobs page
	THEN I should not be able to load the page
	"""
	with function_test_client as c:
		response = function_test_client.get('/jobs')
		assert response.status_code == 401

	"""
	GIVEN a Flask application configured for testing AND I am logged in
	WHEN I try to load the edit jobs page
	THEN I should be able to AND I should see the right content
	"""
	with logged_in_client as c:
		response2 = logged_in_client.get('/jobs')
		assert response2.status_code == 200
		assert b"Add Job</a>" in response2.data
		assert b"Marketly" in response2.data

def test_add_job_page(function_test_client, new_user):
	"""
	GIVEN a Flask application configured for testing AND I am not logged in
	WHEN I try to load the add job page
	THEN I should not be able to load the page
	"""
	with function_test_client as c:
		response = function_test_client.get('/add_job')
		assert response.status_code == 401

		"""
		GIVEN a Flask application configured for testing AND I am logged in
		WHEN I try to load the add job page
		THEN I should be able to AND I should see the right content
		"""

		response_2 = function_test_client.post('/auth/login',
										data=dict(username='freddy function user', password='password1'), follow_redirects=True)
		response_3 = function_test_client.get('/add_job')
		assert response_3.status_code == 200
		assert b"<form action=\"/add_job\" method=\"post\" class=\"form\" role=\"form\">" in response_3.data

def test_add_new_job(logged_in_client):
	"""
	GIVEN a logged in user
	WHEN I add a job with all of the right fields
	THEN the job should be visible on the jobs page
	"""
	with logged_in_client as c:
		data = {
        'company': 'Facebook',
        'start_date': datetime(2018, 1, 1, 0, 0 ,0),
        'end_date': datetime(2020,1,1,0,0,0),
        'job_title': 'News Feed Cleaner',
        'description': 'I was responsible for cleaning the news feed of undesirable and explicit content. During this time \
        				I improved news feed cleanliness by over 75% which helped contribute to Facebook\'s industry award of \
        				Cleaner Social Media Company 2019'
        }
		response = logged_in_client.post('/add_job', data=data, follow_redirects=True)
		assert response.status_code == 200
		assert request.path == url_for('admin.jobs')
		assert b"Facebook" in response.data
		assert b"News Feed Cleaner" in response.data

def test_remove_job(logged_in_client):
	"""
	GIVEN a logged in user with a job
	WHEN I try to remove that job
	THEN job should be succesfully removed
	"""
	with logged_in_client as c:
		response = logged_in_client.get('/jobs')
		assert current_user.jobs != []
		assert response.status_code == 200
		job_id = current_user.jobs[0].oid
		response = logged_in_client.post(f'/remove_job?job_id={job_id}', follow_redirects=True)
		assert current_user.jobs == []