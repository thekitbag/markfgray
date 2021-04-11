def test_career_page(test_client, user_with_job):
	"""
	GIVEN a Flask application configured for testing
	WHEN I try to load the career page
	THEN I should see the right content
	"""
	
	response = test_client.get('/career')
	assert response.status_code == 200
	assert b"<h4>Career Journey</h4>" in response.data
	assert b"<h6>Click a tile to read more</h6>" in response.data