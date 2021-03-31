from webapp.models import User

def test_new_user():
	"""
	GIVEN a User model
	WHEN a new User is created
	THEN check the email, hashed_password, and role fields are defined correctly
	"""
	user = User(username='mark')
	user.set_password('password1')

	assert user.username == 'mark'
	assert user.pwd_hash != 'password1'
	