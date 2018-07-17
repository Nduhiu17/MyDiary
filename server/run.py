from flask import Flask, json
from flask_restful import Resource, Api

from server.models import Entry

app = Flask(__name__)
api = Api(app)


def seeding():
    new_entry = Entry("got guitar", "second hand guitar yamaha", '234567')
    new_entry.save()


class EntryResource(Resource):
    def get(self):
        results = Entry.get_all_entries()
        print("###################################")
        print(results)
        return results


api.add_resource(EntryResource, '/api/v1/entries')

if __name__ == '__main__':
    seeding()
    app.run(debug=True)
