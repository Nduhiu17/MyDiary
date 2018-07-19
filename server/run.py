from urllib import response
from flask import Flask, request, abort
from flask_restful import Resource, Api, reqparse

from models import Entry

app = Flask(__name__)

api = Api(app)


def seeding():
    new_entry = Entry("got guitar", "second hand guitar yamaha", '234567')
    new_entry.save()
    new_entry = Entry("bought a laptop", "second hand from olx seller", '244567')
    new_entry.save()
    new_entry = Entry("learnt react", "learnt how to consume apis with react", '254567')
    new_entry.save()
    new_entry = Entry("test", "its working", '252567')
    new_entry.save()


class EntrylistResource(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'title',
            required=True,
            help='No title provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'description',
            required=True,
            help='No description provided',
            location=['form', 'json']
        )

    def get(self):
        results = Entry.get_all_entries()
        print("###################################")
        # print(results[0])
        return results

    def post(self):
        if not request.json:
            abort(400)
        entry = Entry(title=request.json['title'], description=request.json['description'],
                      date_created=request.json['date_created'])
        print("hello andela")
        print(type(entry))
        entry.save()
        entry_justified = entry.__dict__
        return {"status": "Success", "data": entry_justified}, 201


class EntryResource(Resource):
    def get(self, id):
        result = Entry.get_entry(id)
        result_jsonified = result.__dict__
        print(result_jsonified)
        return result_jsonified


api.add_resource(EntrylistResource, '/api/v1/entries/', methods=['POST', 'GET'])
api.add_resource(EntryResource, '/api/v1/entries/<int:id>', endpoint='entry')

if __name__ == '__main__':
    seeding()
    app.run(debug=True)
