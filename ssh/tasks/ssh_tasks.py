from ssh.ssh_service import SshService
from dao.device_service import DeviceService
from celery import states
from celery.exceptions import NotRegistered,Ignore
from ssh.celery_app import create_celery_app
# from ssh.celery_app import celery                 # for creating celery variable in celery_app file and also add
                                                   # celery.autodiscover function as commented in the ssh.celery_app.py file

celery, app = create_celery_app()


@celery.task(name='ssh.tasks.ssh_tasks.run_commands_on_device', bind=True)
def run_commands_on_device(self, device_id, command):
    if device_id is not None:
        device_service = DeviceService()
        device = device_service.get_device(device_id)
        if 'hostname' in device.keys():
            ssh_service = SshService(device_id)
            ssh_client = ssh_service.connect(device)
            if ssh_client:
                result = ssh_service.run_command(command)
                ssh_service.disconnect()
                self.update_state(state='PROGRESS',
                                  meta={'status': result})
            else:
                self.update_state(state=states.FAILURE,
                                  meta={'status': "Device credential are not correct or device is not up"})
                result = "Device credential are not correct or device is not up"
                # raise Ignore
                # return {"Message": "SSH connection failed"}
        else:
            self.update_state(state=states.FAILURE,
                              meta={'status': "Device Not registered yet"})
            result = "Device Not registered yet"
            # raise Ignore()
    else:
        self.update_state(state=states.FAILURE,
                          meta={'status': "Hostname is required"})
        result = "Hostname is required"
        # return {"Message": "Hostname is none"}, 200

    return {'status': 'Task completed!', 'result': result}
