from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restplus import Api

from app.models import Entry
from app.resources import EntryResource, UserLoginResource, UserRegistrationResource, DeleteResource, OneEntryResource, \
    PutResource
from app.users import UserResource
import psycopg2


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'toomanysecrets' 
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
api.add_resource(OneEntryResource, '/api/v1/entries/<int:id>','/api/v1/entries/<int:id>','/api/v1/entries/<int:id>')
api.add_resource(EntryResource, '/api/v1/entries/', '/api/v1/entries/', '/api/v1/entries/<int:id>')
api.add_resource(DeleteResource, '/api/v1/entries/<int:id>')
api.add_resource(PutResource, '/api/v1/entry/<int:id>')




from . import resources, models
