from flask import request
from dao.user_service import UserService
from web.users import users
from web.common.exceptions import BadRequest

import json

user_service = UserService()


# ############################################# User ############################################################
@users.route('/user', methods=['GET'])
def get_user():
    email = request.args.get('email')
    if email is None or email == "":
        raise BadRequest("Email is required in args")

    result = user_service.get_user(email)
    return result


@users.route('/user', methods=['POST'])             # Not deal with Duplicate Primary key
def register_user():
    new_user = json.loads(request.data)
    if 'email' not in new_user.keys() or 'name' not in new_user.keys():
        raise BadRequest("Email and Name is required in payload")
    result = user_service.add_new_user(new_user)
    return result


@users.route('/user', methods=['PUT'])
def update_user():
    update_user = json.loads(request.data)
    if 'email' not in update_user.keys() or 'name' not in update_user.keys():
        raise BadRequest("Email and Name is required in payload")
    result = user_service.update_user(update_user)
    return result


@users.route('/user', methods=['DELETE'])
def delete_user():
    delete_user = request.args.get('email')
    if 'email' not in delete_user.keys():
        raise BadRequest("Email is required in args")
    result = user_service.delete_user(delete_user)
    return result


@users.route('/users', methods=['GET'])
def get_users():
    result = user_service.get_all_users()
    return result
