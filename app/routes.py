from app import app
import json
from flask import request, jsonify
from app.models import User, Device


@app.route('/device', methods=['GET'])
def get_device():
    ssh_key = request.args.get('ssh_key')
    device = Device.objects(ssh=ssh_key).first()
    if not device:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(device.to_json())


@app.route('/device/all', methods=['GET'])
def get_devices():
    name = request.args.get('name')
    devices = Device.objects(name=name).all()
    if not devices:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(devices)


@app.route('/device', methods=['POST'])
def register_device():
    record = json.loads(request.data)
    device = Device(
            name=record['name'],
            username=record['username'],
            hostname=record['hostname'],
            password=record['password'],
            ssh=record['ssh-key'],
            passphrase=record['passphrase']
        )
    device.save()
    return jsonify(device.to_json())


@app.route('/device', methods=['PUT'])
def update_device():
    record = json.loads(request.data)
    user = User.objects(ssh=record['ssh-key']).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.update(email=record['email'])
    return jsonify(user.to_json())


@app.route('/device', methods=['DELETE'])
def delete_device():
    record = json.loads(request.data)
    device = Device.objects(name=record['name']).first()
    if not device:
        return jsonify({'error': 'data not found'})
    else:
        device.delete()
    return jsonify(device.to_json())

@app.route('/user', methods=['GET'])
def get_user():
    name = request.args.get('name')
    user = User.objects(name=name).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(user.to_json())


@app.route('/user', methods=['POST'])
def register_user():
    record = json.loads(request.data)
    user = User(name=record['name'],
                email=record['email'])
    user.save()
    return jsonify(user.to_json())


@app.route('/user', methods=['PUT'])
def update_user():
    record = json.loads(request.data)
    user = User.objects(name=record['name']).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.update(email=record['email'])
    return jsonify(user.to_json())


@app.route('/user', methods=['DELETE'])
def delete_user():
    record = json.loads(request.data)
    user = User.objects(name=record['name']).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.delete()
    return jsonify(user.to_json())
