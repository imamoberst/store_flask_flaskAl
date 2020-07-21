import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegistration(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="username cannot be blank")
    parser.add_argument('password', type=str, required=True, help="password cannot be blank")

    def post(self):
        data = UserRegistration.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message": "username already exist"}, 400
        user = UserModel(**data)
        user.save_to_db()

        return {"message": "ok done"}, 201
