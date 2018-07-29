import os


class Config:
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    connect_str = "dbname='diary_db' user='postgres' host='localhost' " + "password='postgres'"
    os.environ['DATABASE_URL'] = connect_str


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    # 'test': TestConfig
}
