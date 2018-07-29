import os


class Config:
    # MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    # MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    connect_str = "dbname='diary_db_test' user='postgres' host='localhost' " + "password='postgres'"
    os.environ['DATABASE_URL'] = connect_str


class TestConfig(Config):
    DEBUG = True
    connect_str = "dbname='diary_db_test' user='postgres' host='localhost' " + "password='postgres'"
    os.environ['DATABASE_URL'] = connect_str


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
