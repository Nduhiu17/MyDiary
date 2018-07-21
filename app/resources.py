from flask_restful import Resource, Api, reqparse
from flask import Flask, request, abort,jsonify
from flask_restful import Resource, Api
from .models import Entry


class EntryResource(Resource):
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


    def put(self,id):
        entry = Entry.get_entry(id)
        entry.title =  request.json.get('title')
        entry.description =  request.json.get('description')
        entry.date_created = request.json.get('date_created')
        print("gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg")
        print(entry)
        entry.save()
        entry_jsony = entry.__dict__
        return {"status": "Success", "data":entry_jsony}, 201
  
class OneEntryResource(Resource):
    def get(self, id):
        result = Entry.get_entry(id)
        result_jsonified = result.__dict__
        print(result_jsonified)
        return result_jsonified

class HelloAndela(Resource):
    def get(self):
        return {'Hello': 'Welcome to my second challege product'}


