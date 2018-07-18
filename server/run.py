from flask import Flask
from flask_restful import Resource, Api, reqparse
# from server.models import Entry
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


class EntrylistResource(Resource):
    def get(self):
        results = Entry.get_all_entries()
        print("###################################")
        # print(results[0])
        return results


class EntryResource(Resource):
    def get(self, id):
        result = Entry.get_entry(id)
        result_jsonified = result.__dict__
        print(result)
        return result_jsonified


api.add_resource(EntryResource, '/api/v1/entries/<int:id>', endpoint='entries')
api.add_resource(EntrylistResource, '/api/v1/entries')


if __name__ == '__main__':
    seeding()
    app.run(debug=True)
