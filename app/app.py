from flask import Flask
from flask_restplus import Api
from app.main.resources import OneEntryResource, EntryResource
from config import config_options
from database import Database

db = Database()
api = None


def create_app(config_name):
    print("config name", config_name)
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    # db.__init__()

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    api = Api(app)
    # api.init_app(app)
    app.debug = True
    api.add_resource(OneEntryResource, '/api/v1/entries/<int:id>')
    api.add_resource(EntryResource, '/api/v1/entries/', '/api/v1/entries/', '/api/v1/entries/<int:id>')

    return app
