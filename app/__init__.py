from flask import Flask
from flask_restplus import Api
import psycopg2

from app.models import Entry
from app.resources import EntryResource
from app.resources import EntryResource, OneEntryResource
import psycopg2


app = Flask(__name__)
try:
    connect_str = "dbname='diary_db' user='antony' host='localhost' " + \
                  "password='password'"
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
except Exception as e:
    print("failed to connect db")
    print(e)


api = Api(app)
app.debug = True
api.add_resource(OneEntryResource, '/api/v1/entries/<int:id>')
api.add_resource(EntryResource, '/api/v1/entries/', '/api/v1/entries/', '/api/v1/entries/<int:id>')



from . import resources, models
