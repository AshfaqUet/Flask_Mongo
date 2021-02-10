from dao.device_service import DeviceService
from ssh.ssh_service import SshService

class BaseOs:

    def __init__(self, os, device_id=None):
        self.device_service = DeviceService()
        self.ssh_service = SshService()
        self.__package_manger = ""
        self.OS = os
        self.command = None
        self.device_id = device_id

    # def get_users(self):
    #     pass
    #
    # def list_processes(self):
    #     pass


    def execute_command(self, command: str):
        from ssh.tasks.ssh_tasks import run_commands_on_device

        task = run_commands_on_device.apply_async(args=[self.device_id, command])
        """
        takes a commands and execute it over ssh
        :param command:
        :return:
        """
        return task
        #
        # try:
        #     execute the command
        # except MachineNotFound:
        #     return
