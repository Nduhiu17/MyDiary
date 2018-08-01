from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restplus import Api

from app.models import Entry
from app.resources import EntryResource, UserLoginResource, UserRegistrationResource
from app.resources import EntryResource, OneEntryResource
from app.users import UserResource
import psycopg2


app = Flask(__name__)
jwt = JWTManager(app)
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

api.add_resource(UserRegistrationResource, '/api/v1/register/')
api.add_resource(UserLoginResource, '/api/v1/login/')
api.add_resource(OneEntryResource, '/api/v1/entries/<int:id>')
api.add_resource(EntryResource, '/api/v1/entries/', '/api/v1/entries/', '/api/v1/entries/<int:id>')



from . import resources, models
