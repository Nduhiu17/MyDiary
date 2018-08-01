from flask import request, abort
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restplus import Resource, reqparse
from datetime import datetime

from .models import Entry
from .models import User

parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)


class EntryResource(Resource):
    """Method to get all entries(GET request)"""

    def get(self):
        results = Entry.get_all_entries()
        return results

    def post(self):
        """Method to add an entry(POST request)"""
        if not request.json:
            abort(400)

        entry = Entry.save(user_id=request.json['user_id'], date_created=str(datetime.now()),
                           date_modified=str(datetime.now()), title=request.json['title'],
                           description=request.json['description'])

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


class UserRegistrationResource(Resource):
    def post(self):
        user = User.save(username=request.json['username'],  email=request.json['email'],password=request.json['password'])

        return {"status": "Registered", "data": user}, 201

        # data = parser.parse_args()
        # if User.find_by_username(data['username']):
        #     return {'message': 'User {} already exists'.format(data['username'])}

        # new_user = User.save(username=request.json['username'], email=request.json['email'],
                             # password=request.json['password'])
        # print(data['new_user'])
        # return {"status": "Registered", "data": new_user}, 201
        # try:
        #     # new_user.save_to_db()
        #     access_token = create_access_token(identity=data['username'])
        #     refresh_token = create_refresh_token(identity=data['username'])
        #
        #     return {
        #                'message': 'User {} was created'.format(data['username']),
        #                'access_token': access_token,
        #                'refresh_token': refresh_token
        #            }, 201
        #
        # except:
        #     return {
        #                'message': 'Something went wrong'
        #            }, 500


class UserLoginResource(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = User.find_by_username(data['username'])
        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}

        if User.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity=data['username'])
            refresh_token = create_refresh_token(identity=data['username'])

            return {
                'message': 'Logged in as {}'.format(current_user.username),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        else:
            return {'message': 'Wrong credentials'}
