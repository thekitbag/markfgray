
def test_home_page(test_client):
	"""
	GIVEN a Flask application configured for testing
	WHEN I try to load the home page
	THEN I should see the right content
	"""

	"""
	GIVEN a Flask application configured for testing
	WHEN I try to load the home page
	THEN I should see the right content
	"""
	
	response = test_client.get('/')
	assert response.status_code == 200
	assert b"<h1>Home</h1>" in response.data
	assert b"<h4>Coming soon...</h4>" in response.data
	assert b'<nav class="navbar navbar-expand-lg navbar-light bg-light">' in response.data

def test_admin_page(test_client):
	"""
	GIVEN a Flask application configured for testing
	WHEN I try to load the admin page
	THEN I should see the right content
	"""
	response = test_client.get('/admin')
	assert response.status_code == 200
	assert b'<h1>Admin</h1>' in response.data
	assert b">Register</a>" in response.data
	assert b">Login</a>" in response.data
	assert b">New Blog Post</a>" in response.data
	assert b">Edit Jobs</a>" in response.data

def test_blog_page(test_client):
	"""
	GIVEN a Flask application configured for testing
	WHEN I try to load the blog page
	THEN I should see the right content
	"""
	response = test_client.get('/blog')
	assert response.status_code == 200
	assert b'<h1>Blog</h1>' in response.data
	assert b"<h4>Coming soon...</h4>" in response.data

def test_login_page(test_client):
	"""
	GIVEN a Flask application configured for testing
	WHEN I try to load the login page
	THEN I should see the right content
	"""
	response = test_client.get('/auth/login')
	assert response.status_code == 200
	assert b"<h2>Welcome back</h2>" in response.data

def test_personal_page(test_client):
	"""
	GIVEN a Flask application configured for testing
	WHEN I try to load the personal page
	THEN I should see the right content
	"""
	response = test_client.get('/personal')
	assert response.status_code == 200
	assert b'<h1>Away From Work</h1>' in response.data
	assert b"<h4>Coming soon...</h4>" in response.data

def test_register_page(test_client):
	"""
	GIVEN a Flask application configured for testing
	WHEN I try to load the register page
	THEN I should see the right content
	"""
	response = test_client.get('/auth/register')
	assert response.status_code == 200
	assert b"<h2>Register</h2>" in response.data

def test_skills_page(test_client):
	"""
	GIVEN a Flask application configured for testing
	WHEN I try to load the skills page
	THEN I should see the right content
	"""
	response = test_client.get('/skills')
	assert response.status_code == 200
	assert b"<h1>Skills</h1>" in response.data
	assert b"<h4>Coming soon...</h4>" in response.data

def test_tools_page(test_client):
	"""
	GIVEN a Flask application configured for testing
	WHEN I try to load the tools page
	THEN I should see the right content
	"""
	response = test_client.get('/tools')
	assert response.status_code == 200
	assert b"<h1>Tools</h1>" in response.data
	assert b"<h4>Coming soon...</h4>" in response.data


