from flask_restful import Resource, Api, reqparse
from flask import Flask, request, abort,jsonify
from flask_restful import Resource, Api
from .models import Entry


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


class Hello(Resource):
    def get(self):
        all_entrys = Entry.get_all_entries()
        return {'Hello'}


