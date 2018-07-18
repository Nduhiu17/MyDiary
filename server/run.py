from flask import Flask, json
from flask_restful import Resource, Api

from .models import Entry

app = Flask(__name__)
api = Api(app)


def seeding():
    new_entry = Entry("got guitar", "second hand guitar yamaha", '234567')
    new_entry.save()
    new_entry = Entry("bought a laptop", "second hand from olx seller", '244567')
    new_entry.save()
    new_entry = Entry("learnt react", "learnt how to consume apis with react", '254567')
    new_entry.save()


class EntryResource(Resource):
    def get(self):
        results = Entry.get_all_entries()
        print("###################################")
        print(results)
        return results

   # def get_by_id(self):
   #     result = Entry.get_entry()



api.add_resource(EntryResource, '/api/v1/entries')
# api.add_resource(EntryResource, '/api/v1/entries/id')

if __name__ == '__main__':
    seeding()
    app.run(debug=True)
