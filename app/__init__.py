from flask import Flask
from flask_restful import Api
from flask_marshmallow import Marshmallow
from .models import Entry
from .resources import EntrylistResource, EntryResource,HelloAndela


app = Flask(__name__)





app.debug = True
ma = Marshmallow(app)
api = Api(app)
# app = create_app('config')

from . import resources, models