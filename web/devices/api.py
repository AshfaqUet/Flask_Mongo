from flask import request, Response
from dao.device_service import DeviceService
from web.devices import devices


import json


# ############################################ device ###########################################################

device_service = DeviceService()


@devices.route('/index', methods=['GET'])
def index():
    return {"message":"Hello World"}


@devices.route('/device', methods=['GET'])
def get_device():
    hostname = request.args.get('hostname')
    # Exception in this request
    if hostname is None:
        return Response(status=400)
    result = device_service.get_device(hostname)
    return result


@devices.route('/devices', methods=['GET'])
def get_devices():
    device = json.loads(request.data)
    # Exception in this request
    if device['name'] is None:
        return Response(status=400)
    result = device_service.get_all_devices(device['name'])
    return result


@devices.route('/device', methods=['POST'])         # Not deals with duplicate primary key
def register_device():
    new_device = json.loads(request.data)
    # Exception in this request
    if new_device['hostname'] is None:
        return Response(status=400)

    result = device_service.add_new_device(new_device)
    return result


@devices.route('/device', methods=['PUT'])
def update_device():
    update_device = json.loads(request.data)
    # Exception in this request
    if update_device['hostname'] is None:
        return Response(status=400)
    result = device_service.update_device(update_device)
    return result


@devices.route('/device', methods=['DELETE'])
def delete_device():
    delete_user = json.loads(request.data)
    # Exception in this request
    if delete_user['hostname'] is None:
        return Response(status=400)
    result = device_service.delete_device(delete_device)
    return result
