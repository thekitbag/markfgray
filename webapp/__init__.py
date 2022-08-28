from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from config import Config

bootstrap = Bootstrap()
login = LoginManager()
db = MongoEngine()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    login.init_app(app)
    bootstrap.init_app(app)

    from webapp.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from webapp.main import bp as main_bp
    app.register_blueprint(main_bp)

    from webapp.admin import bp as admin_bp
    app.register_blueprint(admin_bp)

    return app

from webapp import models
