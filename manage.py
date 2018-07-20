from urllib import response
from flask import Flask, request, abort
from flask_restful import Resource, Api, reqparse
from app.models import Entry
from app.resources import EntryResource, EntrylistResource, HelloAndela
# from app import create_app,seeding

app = Flask(__name__)

api = Api(app)

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

if __name__ == '__main__':
    app = create_app("config")
    seeding()
    app.run()
