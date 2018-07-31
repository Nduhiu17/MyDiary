import datetime

class Config(object):
    DEBUG = True
    TESTING = True
    CSRF_ENABLED = True
    APP_NAME = 'MyDiary'



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
