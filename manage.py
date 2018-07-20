from urllib import response
from flask import Flask, request, abort
from flask_restful import Resource, Api, reqparse
from app.models import Entry
from app.resources import EntryResource, EntrylistResource
from app import create_app,seeding

app = Flask(__name__)

api = Api(app)


if __name__ == '__main__':
    app = create_app("config")
    seeding()
    app.run()
