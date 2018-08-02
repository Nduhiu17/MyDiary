from flask import request, abort
from flask_jwt_extended import create_access_token, jwt_required
from flask_restplus import Resource, reqparse
from datetime import datetime

from .models import Entry
from .models import User


class EntryResource(Resource):
    """Method to get all entries(GET request)"""

    # @jwt_required
    def get(self):
        results = Entry.get_all_entries()
        return results

    # @jwt_required
    def post(self):
        """Method to add an entry(POST request)"""
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', help='This field cannot be blank', required=True)
        parser.add_argument('title', help='This field cannot be blank', required=True)
        parser.add_argument('description', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        if not request.json:
            abort(400)

        entry = Entry.save(user_id=data['user_id'], date_created=str(datetime.now()),
                           date_modified=str(datetime.now()), title=data['title'],
                           description=data['description'])

        return {"status": "Success", "data": entry}, 201

    # def delete(self,id):
    #     """Method to delete an entry(DELETE request)"""
    #     entry = Entry.get_entry(id)
    #     entry.delete()
    #     entry.save()
    #     return {"status": "Success"}, 200


class OneEntryResource(Resource):
    """Method to get an entry by id(GET request)"""

    @jwt_required
    def get(self, id):
        result = Entry.get_entry(id)
        return result


class PutResource(Resource):
    def put(self, id):
        """Method to edit an entry(PUT request)"""
        # entry = Entry.get_entry(id)
        # entry[0] = request.json.get('user_id')
        # entry[1] = request.json.get('title')
        # entry[2] = request.json.get('description')
        # entry.save()
        # entry_jsony = entry.__dict__
        entry = Entry.update(
            title=request.json['title'],
            description=request.json['description'],
            id=id)
        return {"status": "Success", "data": entry}, 201


# @api.route('/delete')
class DeleteResource(Resource):

    def delete(self, id):
        status = Entry.delete(id)
        if status:
            return {"status": status}, 200
        else:
            return {'status': status}, 500


class UserRegistrationResource(Resource):
    def post(self):
        # parser = reqparse.RequestParser()
        # parser.add_argument('username', help='This field cannot be blank', required=True)
        parser = reqparse.RequestParser()
        parser.add_argument('username', help='This field cannot be blank', required=True)
        parser.add_argument('password', help='This field cannot be blank', required=True)
        parser.add_argument('email', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        user = User.save(username=data['username'], email=data['email'],
                         password=User.generate_hash(data['password']))

        return user, 201


class UserLoginResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('password', help='This3 field cannot be blank', required=True)
        parser.add_argument('email', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        current_user = User.find_by_email(data['email'])
        print("user in db",current_user)
        if current_user == False:
            return {'message': 'User {} doesn\'t exist'.format(data['email'])}

        if User.verify_hash(data['password'], current_user[3]):
            access_token = create_access_token(identity=data['email'])
            return {
                'message': 'Logged in as {}'.format(current_user[1]),
                'access_token': access_token,
            }
        else:
            return {'message': 'Wrong credentials'}
