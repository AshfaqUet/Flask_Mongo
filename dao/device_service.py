import logging
from models.device_models import Device

logger = logging.getLogger("dao.device_service")

class DeviceService:
    def __init__(self):
        self.devices = Device
        self.devices_list = list()

    def get_device(self,hostname):
        self.devices = Device.objects(hostname=hostname).first()
        if not self.devices:
            return {'error': 'data not found'}
        else:
            return self.devices.to_json()

    def get_all_devices(self,device_name):
        self.devices_list = Device.objects(name=device_name).all()
        if not self.devices_list:
            return {'error': 'data not found'}
        else:
            return self.devices_list

    def add_new_device(self,device_info):
        self.devices = Device(
            name=device_info['name'],
            username=device_info['username'],
            hostname=device_info['hostname'],
            password=device_info['password'],
            ssh=device_info['ssh'],
            passphrase=device_info['passphrase']
        )
        self.devices.save()
        return self.devices.to_json()

    def update_device(self,device_info):
        self.devices = Device.objects(hostname=device_info['hostname']).first()
        if not self.devices:
            return {'error': 'device not found'}
        else:
            self.devices.update(hostname=device_info['hostname'])
            for key, value in self.devices.to_json().items():
                if key in device_info.keys():
                    self.devices[key] = device_info[key]
            self.devices.update(
                name=self.devices.to_json()["name"],
                username=self.devices.to_json()["username"],
                hostname=self.devices.to_json()["hostname"],
                password=self.devices.to_json()["password"],
                ssh=self.devices.to_json()["ssh"],
                passphrase=self.devices.to_json()["passphrase"]
            )

        return self.devices.to_json()

    def delete_device(self,device_info):
        self.devices = Device.objects(hostname=device_info['hostname']).first()
        if not self.devices:
            return {'error': 'data not found'}
        else:
            self.devices.delete()
        return self.devices.to_json()
