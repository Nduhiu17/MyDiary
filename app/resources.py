from flask import request, abort
from flask_jwt_extended import create_access_token
from flask_restplus import Resource, reqparse
from datetime import datetime

from .models import Entry
from .models import User


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
        parser = reqparse.RequestParser()
        parser.add_argument('username', help='This field cannot be blank', required=True)
        user = User.save(username=request.json['username'], email=request.json['email'],
                         password=User.generate_hash(request.json['password']))

        return {"status": "Registered", "data": user}, 201


class UserLoginResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('password', help='This3 field cannot be blank', required=True)
        parser.add_argument('email', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        current_user = User.find_by_email(data['email'])
        print(current_user)
        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['email'])}
        elif User.verify_hash("passworddgx", current_user[3]):
            access_token = create_access_token(identity=data['email'])
            print("the token is here")
            print(access_token)
            return {
                'message': 'Logged in as {}'.format(current_user.email),
                'access_token': access_token,
            }
        else:
            return {'message': 'Wrong credentials'}
