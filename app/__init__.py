from flask import Flask
from flask_restplus import Api
import psycopg2

from app.models import Entry
from app.resources import EntryResource
from app.resources import EntryResource, OneEntryResource

app = Flask(__name__)

# cursor = ''
# try:
#     connect_str = "dbname='diary_db' user='antony' host='localhost' " + \
#                   "password='password'"
#     # use our connection values to establish a connection
#     conn = psycopg2.connect(connect_str)
#     # create a psycopg2 cursor that can execute queries
#     cursor = conn.cursor()
#     # cursor.execute('SELECT * FROM "public"."entries"')
#     # rows = cursor.fetchall()
#     # print(rows)
#     print("db connectd!!!")
# except Exception as e:
#     print("Uh oh, can't connect. Invalid dbname, user or password?")
#     print(e)

api = Api(app)
app.debug = True
api.add_resource(OneEntryResource, '/api/v1/entries/<int:id>')
api.add_resource(EntryResource, '/api/v1/entries/', '/api/v1/entries/', '/api/v1/entries/<int:id>')


def seeding():
    new_entry = Entry("got guitar", "second hand guitar yamaha", '234567')
    new_entry.save()
    new_entry = Entry("bought a laptop", "second hand from olx seller", '244567')
    new_entry.save()
    new_entry = Entry("learnt react", "learnt how to consume apis with react", '254567')
    new_entry.save()
    new_entry = Entry("test", "its working", '252567')
    new_entry.save()


seeding()
from . import resources, models
