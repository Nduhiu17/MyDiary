# from flask import Flask
# from flask_restplus import Api
# # import psycopg2
# from app.main.resources import OneEntryResource, EntryResource
# from app.models import Entry
# # from app.resources import EntryResource
# # from app.resources import EntryResource, OneEntryResource
# # import psycopg2
# from config import config_options
# from database import Database
#
# # app = Flask(__name__)
# # try:
# #     connect_str = "dbname='diary' user='antony' host='localhost' " + \
# #                   "password='password'"
# #     # use our connection values to establish a connection
# #     conn = psycopg2.connect(connect_str)
# #     # create a psycopg2 cursor that can execute queries
# #     cursor = conn.cursor()
# #     # create a new table with a single column called "name"
# #     cursor.execute("""CREATE TABLE tutorials (name char(40));""")
# #     # run a SELECT statement - no data in there, but we can try it
# #     cursor.execute("""SELECT * from tutorials""")
# #     rows = cursor.fetchall()
# #     print(rows)
# # except Exception as e:
# #     print("failed to connect db")
# #     print(e)
# db = Database()
# api = None
# def create_app(config_name):
#     app = Flask(__name__)
#     # db = Database()
#
#     app.config.from_object(config_options[config_name])
#     # app.config.from_object(app_config[config_name])
#     db.__init__()
#     # from Api_v1.app.endpoints.contents import entries_namespace as entries
#     # from Api_v1.app.endpoints.auth import auth_namespace as auth
#     # api.add_namespace(entries, path='/user')
#     # api.add_namespace(auth, path='/auth')
#     # api.init_app(app)
#     # JsonExceptionHandler(app)
#     from .main import main as main_blueprint
#     app.register_blueprint(main_blueprint)
#
#     api = Api(app)
#     app.debug = True
#     api.add_resource(OneEntryResource, '/api/v1/entries/<int:id>')
#     api.add_resource(EntryResource, '/api/v1/entries/', '/api/v1/entries/', '/api/v1/entries/<int:id>')
#
#     return app
#
# # api = Api(app)
# # app.debug = True
# # api.add_resource(OneEntryResource, '/api/v1/entries/<int:id>')
# # api.add_resource(EntryResource, '/api/v1/entries/', '/api/v1/entries/', '/api/v1/entries/<int:id>')
#
#
#
# # from . import  models
