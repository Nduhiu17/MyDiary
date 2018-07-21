import datetime
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    REMEMBER_COOKIE_DURATION = datetime.timedelta(days=14)
    DEBUG = True
    TESTING = True
    CSRF_ENABLED = True
    # SECRET_KEY = 'andela-july-2018'


class ProductionConfig(Config):
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False


config_environments = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
