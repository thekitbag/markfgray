from webapp.models import User
from flask import request, url_for
from flask_login import current_user
from datetime import datetime

def test_login(function_test_client, new_user):
	"""
	GIVEN incorrect login details
	WHEN I try to log in
	THEN I should see an error message and stay on the login page
	"""

	with function_test_client as c:
		response = function_test_client.post('/auth/login',
									data=dict(username='made up user', password='123456')) 
		assert response.status_code == 302

		response_2 = function_test_client.post('/auth/login',
									data=dict(username='made up user', password='123456'), follow_redirects=True) 
		assert response_2.status_code == 200
		assert current_user.is_authenticated == False
		assert b"Invalid login details" in response_2.data

	"""
	GIVEN correct login details
	WHEN I try to log in
	THEN I should be rediredted to the admin page
	"""
	with function_test_client as c:
		response_3 = function_test_client.post('/auth/login',
									data=dict(username='freddy function user', password='password1'), follow_redirects=True) 
		assert response_3.status_code == 200
		assert current_user.is_authenticated == True
		assert b'<h1>Admin</h1>' in response_3.data
		assert b">Register</a>" in response_3.data
		assert b">Login</a>" in response_3.data
		assert b">Blog Posts</a>" in response_3.data

def test_register(new_user, function_test_client):
	"""
	GIVEN a username that is not taken
	WHEN I try to register with a username and password
	THEN I should be succesful
	"""
	with function_test_client as c:
		data = {
        'username': 'shannon',
        'password': 'Password1',
        'password2': 'Password1'
        }
		response = function_test_client.post('/auth/register',
									data=data, follow_redirects=True)
		assert response.status_code == 200
		assert request.path == url_for('admin.admin')

	"""
	GIVEN a username that is already taken
	WHEN I try to register with a username and password
	THEN I should be unsuccesful and i should be told to choose a different username
	"""
	with function_test_client as c:
		data = {
        'username': 'freddy function user',
        'password': 'Password1',
        'password2': 'Password1'
        }
		response_2 = function_test_client.post('/auth/register',
									data=data, follow_redirects=True)
		assert response_2.status_code == 200
		assert request.path == url_for('auth.register')
		assert b"Please use a different username" in response_2.data

	"""
	GIVEN I supply passwords that do not match
	WHEN I try to register
	THEN I should be unsuccesful and i should be told to make my passwords match
	"""
	with function_test_client as c:
		data = {
        'username': 'mark',
        'password': 'Password1',
        'password2': 'Password2'
        }
		response_3 = function_test_client.post('/auth/register',
									data=data, follow_redirects=True)
		assert response_3.status_code == 200
		assert request.path == url_for('auth.register')
		assert b"Passwords must match" in response_3.data

def test_logout(function_test_client, new_user):
	"""
	GIVEN I am logged in 
	WHEN I go to the logout URL
	THEN I am logged out
	"""
	with function_test_client as c:
		response = function_test_client.post('/auth/login',
										data=dict(username='freddy function user', password='password1'), follow_redirects=True)
		assert response.status_code == 200
		assert current_user.is_authenticated == True
		response_2 = function_test_client.get('/auth/logout')
		assert current_user.is_authenticated == False






	
		




	