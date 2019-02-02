from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
import datetime


""" local imports """
from models.models import users, Users



""" create class to handle user registration view """


class RegisterUsers(Resource):

    parsing = reqparse.RequestParser(bundle_errors=True)
    parsing.add_argument('firstname', type=str,
                         required=True, help='This field is required')
    parsing.add_argument('lastname', type=str,
                         required=True, help='This field cannot be left empty')
    parsing.add_argument('username', type=str,
                         required=True, help='email field is required field is required')
    parsing.add_argument('password', type=str, required=True,
                         help='Password field cannot be empty')
    parsing.add_argument('email', type=str, required=True,
                         help='email field cannot be empty')

    def post(self):
        user_data = RegisterUsers.parsing.parse_args()

        firstname = user_data['firstname']
        lastname = user_data['lastname']
        username = user_data['username']
        password = user_data['password']
        email = user_data['email']

       
        user = Users(firstname, lastname, username, password, email)
        users.append(user)

        return {"Message": "User registration successful"}, 201

    """ Get all users """
    def get(self):
        return {"Users" : [user.serializer() for user in users]}
     


class Login(Resource):
    parser = reqparse.RequestParser(bundle_errors=True)

    parser.add_argument('email', type=str, required=True,
                        help='Email field cannot be null')
    parser.add_argument('password', type=str, required=True,
                        help='Password field is required')
    def post(self):
        login_data = Login.parser.parse_args()

        email = login_data['email']
        password = login_data['password']

      
        user = Users().get_user_by_email(email)

        if user:
            return {"Message": "You have succesfully logged in"}, 200
        return {"Message" : "user does not exists"}, 400
        
