from datetime import datetime

def test_career_page_basic(test_client, user_with_job):
	"""
	GIVEN a Flask application configured for testing
	WHEN I try to load the career page
	THEN I should see the right content
	"""
	
	response = test_client.get('/career')
	assert response.status_code == 200
	assert b"Over the past 11 years I've held a few different roles across three companies"in response.data

def test_career_page_new_company_new_job(logged_in_client):
	"""GIVEN a logged in user
	WHEN I add a new company and a new job for that company
	THEN I should see that job and all of the relevant details on the career journey page
	"""
	response = logged_in_client.get('/career')
	assert response.status_code == 200
	assert b"<h4>Career Journey</h4>" in response.data
	assert b"a16z" not in response.data
	assert b"Seed Stage Startup Investor" not in response.data

	response2 = logged_in_client.post('/add_company', data={'name': 'a16z'})
	response3 = logged_in_client.post('/add_job', data=dict(
														job_title = 'Seed Stage Startup Investor',
														company = 'a16z',
														start_date = '2010-10-01',
														end_date = '2015-12-25',
														description = 'Invested in 10 seed stage companies in the UK \
														Asia and South America',
														achievements = 'Exited for 1000% profit \n\
														Mentored 6 CEOs \n Won an industry award'
													))
	response4 = logged_in_client.get('/career')
	assert response4.status_code == 200
	assert b"a16z" in response4.data
	assert b"Seed Stage Startup Investor" in response4.data