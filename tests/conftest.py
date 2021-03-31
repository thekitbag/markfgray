import pytest 
import config
from flask.testing import FlaskClient
from webapp.models import User
from webapp import create_app, db


@pytest.fixture(scope='function')
def new_user():
    user = User(username="freddy function user")
    user.set_password('password1')
    user.save()
    yield user
    user.delete()
    
@pytest.fixture(scope='module')
def new_user_module():
    user = User(username="mark module user")
    user.set_password('password1')
    return user

@pytest.fixture(scope='session')
def new_user_session():
    user = User(username="sally function user")
    user.set_password('password1')
    return user


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(config.TestConfig)

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!

@pytest.fixture(scope='function')
def function_test_client():
    flask_app = create_app(config.TestConfig)

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!




@pytest.fixture(scope='function')
def function_test_client():
    flask_app = create_app(config.TestConfig)
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()
    

