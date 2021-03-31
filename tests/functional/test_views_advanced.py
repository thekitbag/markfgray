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

	