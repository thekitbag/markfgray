import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456'
    CACHE_TYPE = "simple" # Flask-Caching related configs
    CACHE_DEFAULT_TIMEOUT = 300

class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    MONGODB_SETTINGS = {
    'db': 'markfaradaygray',
    'host': 'localhost',
    'port': 27017
}
    USERNAME = 'mfg'
    MIXPANEL_ID = '801bb0de9db704f130e05196ab535bd1'

class ProductionConfig(Config):
    DEBUG = False
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    MONGODB_HOST = os.environ.get('MONGODB_URI')
    USERNAME = os.environ.get('USERNAME') or 'mfg'
    MIXPANEL_ID = 'b5cc2c3e2c77a3ae9293b1b4184b55e7'

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    WTF_CSRF_ENABLED = False
    SERVER_NAME = 'localhost.localdomain'
    MAX_POSTS_PER_DAY = 1000
    MAX_POSTS_PER_QUARTER = 1000
    MONGODB_SETTINGS = {
    'db': 'test_markfaradaygray',
    'host': 'localhost',
    'port': 27017
}
    USERNAME = 'mark'