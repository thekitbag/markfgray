from webapp.models import User

def test_new_user(new_user):
	"""
	GIVEN a User model
	WHEN a new User is created
	THEN check the hashed_password and role fields are defined correctly
	"""

	assert new_user.username == 'freddy function user'
	assert new_user.pwd_hash != 'password1'
	assert new_user.check_password('password99') == False
	assert new_user.check_password('password1') == True
	