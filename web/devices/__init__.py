from flask import Blueprint

devices = Blueprint("devices", __name__)

from web.devices import api, ssh_api