import pytest 
import config
from datetime import datetime
from flask.testing import FlaskClient
from webapp.models import User, Job, Company, Post
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


@pytest.fixture(scope='function')
def mark():
    user = User(username="mark")
    user.set_password('password1')
    user.save()
    yield user
    user.delete()


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
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()
    User.objects({}).delete()


@pytest.fixture(scope='function')
def user_with_job():
    u = User(username='mark')
    u.set_password('123')
    j = Job()
    c = Company()
    c.name = 'Marketly'
    c.description = 'Online marketing company'
    c.img_url = 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png'
    c.save()
    j.company = c
    j.start_date = datetime(2018, 1, 1, 0, 0 ,0)
    j.end_date =  datetime(2020, 1, 1, 0, 0, 0)
    j.job_title = 'CEO'
    j.description = 'I ran the comapny from day to day and grew it by 1000% in the first year'
    j.achievements = 'smashed all my targets \
    hired lots of people \
    made all the prcocesses better'
    u.add_job(j)
    u.save()
    yield u
    u.delete()
    c.delete()

@pytest.fixture(scope='function')
def logged_in_client(user_with_job):
    flask_app = create_app(config.TestConfig)
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    response = testing_client.post('/auth/login',
                                        data=dict(username='mark', password='123'), follow_redirects=True)

    yield testing_client  # this is where the testing happens!

    c = db.connect('test_markfaradaygray')
    c.drop_database('test_markfaradaygray')
    ctx.pop()
    

