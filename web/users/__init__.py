from flask import Blueprint

users = Blueprint('users', __name__)

from web.users import api