from urllib import response
from flask import Flask, request, abort
from flask_restful import Resource, Api, reqparse
from app.models import Entry
from app.resources import EntryResource, HelloAndela, OneEntryResource

app = Flask(__name__)

api = Api(app)

api.add_resource(OneEntryResource, '/api/v1/entries/<int:id>')
api.add_resource(EntryResource, '/api/v1/entries/', '/api/v1/entries/', '/api/v1/entries/<int:id>')

api.add_resource(HelloAndela, '/')


def seeding():
    new_entry = Entry("got guitar", "second hand guitar yamaha", '234567')
    new_entry.save()
    new_entry = Entry("bought a laptop", "second hand from olx seller", '244567')
    new_entry.save()
    new_entry = Entry("learnt react", "learnt how to consume apis with react", '254567')
    new_entry.save()
    new_entry = Entry("test", "its working", '252567')
    new_entry.save()


seeding()
if __name__ == '__main__':
    seeding()
    app.run(debug=True, port=5000)
