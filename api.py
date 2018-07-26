from flask import Flask
from flask_restful import Api

from app.models import Entry
from app.resources import EntryResource, OneEntryResource

app = Flask(__name__)

api = Api(app)

api.add_resource(OneEntryResource, '/api/v1/entries/<int:id>')
api.add_resource(EntryResource, '/api/v1/entries/', '/api/v1/entries/', '/api/v1/entries/<int:id>')

if __name__ == '__main__':
    debug = True
    app.run()
