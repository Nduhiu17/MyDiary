from flask import request, abort
from flask_restplus import Resource
from datetime import datetime

from .models import Entry


class EntryResource(Resource):
    """Method to get all entries(GET request)"""
    def get(self):
        results = Entry.get_all_entries()
        return results

    def post(self):
        """Method to add an entry(POST request)"""
        if not request.json:
            abort(400)

        # entry = Entry.save(user_id=request.json['user_id'],title=request.json['title'],description=request.json['description'])
        # entry = Entry.save(user_id=request.json['user_id'],date_created=request.json['date_created'],title=request.json['title'],description=request.json['description'])
        # print("******************", request.json['description'])
        # entry = Entry.save(user_id=request.json['user_id'],date_created = str(datetime.now()),date_modified = str(datetime.now()), title=request.json['title'],description=request.json['description'])
        entry = Entry.save(user_id=request.json['user_id'],date_created = str(datetime.now()),date_modified = str(datetime.now()),title=request.json['title'],description=request.json['description'])

        
        return {"status": "Success", "data": entry}, 201

    # def put(self, id):
    #     """Method to edit an entry(PUT request)"""
    #     entry = Entry.get_entry(id)
    #     entry.title = request.json.get('title')
    #     entry.description = request.json.get('description')
    #     entry.date_created = request.json.get('date_created')
    #     print("gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg")
    #     print(entry)
    #     entry.save()
    #     entry_jsony = entry.__dict__
    #     return {"status": "Success", "data":entry_jsony}, 201

    # def delete(self,id):
    #     """Method to delete an entry(DELETE request)"""
    #     entry = Entry.get_entry(id)
    #     entry.delete()
    #     entry.save()
    #     return {"status": "Success"}, 200
#     #
class OneEntryResource(Resource):
    """Method to get an entry by id(GET request)"""
    def get(self, id):
        result = Entry.get_entry(id)
        return result






