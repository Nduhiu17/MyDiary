from flask import Flask
from flask_restful import Api
from flask_marshmallow import Marshmallow
from .models import Entry
from .resources import EntrylistResource, EntryResource,HelloAndela


app = Flask(__name__)


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    api = Api(app)
    api.add_resource(EntrylistResource, '/api/v1/entries/', methods=['POST', 'GET'])
    api.add_resource(EntryResource, '/api/v1/entries/<int:id>', endpoint='entry')
    api.add_resource(HelloAndela, '/')
    return app

def seeding():
    new_entry = Entry("got guitar", "second hand guitar yamaha", '234567')
    new_entry.save()
    new_entry = Entry("bought a laptop", "second hand from olx seller", '244567')
    new_entry.save()
    new_entry = Entry("learnt react", "learnt how to consume apis with react", '254567')
    new_entry.save()
    new_entry = Entry("test", "its working", '252567')
    new_entry.save()


app.debug = True
ma = Marshmallow(app)
api = Api(app)
app = create_app('config')

from . import resources, models