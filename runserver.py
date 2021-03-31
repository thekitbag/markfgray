#from webapp import app

import os
from webapp import create_app, db
from webapp.models import User
import config

if os.environ['FLASK_ENV'] == 'development':
	app = create_app(config.DevelopmentConfig)
elif os.environ['FLASK_ENV'] == 'prod':
	app = create_app(config.ProductionConfig)
else:
	print('ENV NOT SET TO dev, staging or prod')


@app.shell_context_processor
def make_shell_context():
    return {
    'db': db, 
    'User': User, 
    'u1':User(username='mark')

    }