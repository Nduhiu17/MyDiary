from flask import request, abort
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_restplus import Resource, reqparse
from datetime import datetime,timedelta

from .models import Entry
from .models import User


class EntryResource(Resource):
    # Method to get all entries(GET request)

    @jwt_required
    def get(self):
        # current_user = get_jwt_identity()
        # Retrieve token from headers
        #decode token to get email
        # call get_user_by_email method and pass the email from the decoded token to query from db
        # from the user details returned retrieve the id
        # call the get_all_entries method passing the id as an argument
        # this will return the entries for that user
        results = Entry.get_all_entries()
        return results

    @jwt_required
    def post(self):
        # Method to add an entry(POST request)
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


class OneEntryResource(Resource):
    # Method to get an entry by id(GET request
    @jwt_required
    def get(self, id):
        result = Entry.get_entry(id)
        return result


class PutResource(Resource):
    # Method to modifies an entry(PUT request
    @jwt_required
    def put(self, id):
        entry = Entry.update(
            title=request.json['title'],
            description=request.json['description'],
            id=id)
        return {"status": "Success", "data": entry}, 201


class DeleteResource(Resource):
    # method that deletes an entry
    def delete(self, id):
        status = Entry.delete(id)
        if status:
            return {"status": status}, 200
        else:
            return {'status': status}, 500


class UserRegistrationResource(Resource):
    # Method that registers a user
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', help='This field cannot be blank', required=True)
        parser.add_argument('password', help='This field cannot be blank', required=True)
        parser.add_argument('email', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        print("we are here test",len(data["password"]))
        if len(data["password"]) < 5:
            return {
                "status":"Please enter a password with more than five characters"
            },400
        user = User.save(username=data['username'], email=data['email'],
                         password=User.generate_hash(data['password']))

        return user, 201


class UserLoginResource(Resource):
    
    # Method that logs in a user and creates for him a security token
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('password', help='This3 field cannot be blank', required=True)
        parser.add_argument('email', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        current_user = User.find_by_email(data['email'])
        print("user in db", current_user)
        if current_user == False:
            return {'message': 'User {} doesn\'t exist'.format(data['email'])}

        if User.verify_hash(data['password'], current_user[3]):
            # expires = datetime.now + timedelta(days=365)
            access_token = create_access_token(identity=data['email'])
            return {
                'message': 'Logged in as {}'.format(current_user[1]),
                'access_token': access_token,
            }
        else:
            return {'message': 'Wrong credentials'}
