from flask import request, jsonify, url_for
from dao.device_service import DeviceService
from web.devices import devices
from ssh.supportedOperSys.ubuntu_os import UbuntuOs
from ssh.supportedOperSys.windows_os import WindowsOs

device_service = DeviceService()


@devices.route('/device/os/users', methods=['GET'])
def os_users():
    users = "No Users to show"
    device_id = request.args.get('id')
    device = device_service.get_device(device_id)
    if device['os'] == 'ubuntu':
        linux_device = UbuntuOs(device_id)
        users = linux_device.get_users()
    elif device['os'] == 'windows':
        window_device = WindowsOs(device_id)
        users = window_device.get_users()
    if users is not None:
        url = url_for('devices.taskstatus', task_id=users.id)
        return jsonify({'Location': url}), 202
    else:
        return {"Message": "Task not submitted successfully"}

@devices.route('/device/os/help',methods=['GET'])
def os_help():
    helping_material = "No help"
    device_id = request.args.get('id')
    device = device_service.get_device(device_id)
    if device['os'] == 'ubuntu':
        linux_device = UbuntuOs(device_id)
        helping_material = linux_device.helping_function()
    elif device['os'] == 'windows':
        window_device = WindowsOs(device_id)
        helping_material = window_device.helping_function()
    return helping_material


@devices.route('/device/ssh', methods=['GET'])
def ssh_device():
    task = None
    command = request.args.get('command')
    device_id = request.args.get('id')
    device = device_service.get_device(device_id)
    if device['os'] == 'ubuntu':
        linux_device = UbuntuOs(device_id)
        task = linux_device.execute_command(command)
    elif device['os'] == 'windows':
        window_device = WindowsOs(device_id)
        task = window_device.execute_command(command)
    if task is not None:
        url = url_for('devices.taskstatus',task_id=task.id)
        return jsonify({'Location': url}), 202
    else:
        return {"Message": "Task not submitted successfully"}


@devices.route('/status/<task_id>')
def taskstatus(task_id):
    from ssh.tasks.ssh_tasks import run_commands_on_device
    task = run_commands_on_device.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'status': task.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    elif task.state == 'FAILURE':
        # something went wrong in the background job
        response = {
            'state': task.state,
            'status': str(task.info),  # this is the exception raised
        }
    return jsonify(response)
