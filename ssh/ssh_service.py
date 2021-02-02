from dao.device_service import DeviceService
import paramiko


class SshService:
    def __init__(self,hostname=None):
        self.device_service = DeviceService()
        self.hostname = hostname
        self.command = None
        self.result = None
        self.ssh_client = None


    def run_command_on_host(self,command):
        self.command = command
        device = self.device_service.get_device(self.hostname)
        if device:
            connect = self.connect(device)
            if connect:
                result = self.run_command(self.command)
                self.disconnect()
                return result


    def connect(self, credentials):
        """
        :param: username: Username of the device which you want to ssh/connect
        :param: ip_address: IP address of the device which you want to ssh/connect
        :param: password: Password of the device which you want to ssh/connect
        :return: True / False
        """
        username = credentials['username']
        ip_addr = credentials['hostname']
        password = credentials['password']
        client = paramiko.SSHClient()  # paramiko client object
        client.load_system_host_keys()  # this loads any local ssh keys
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(ip_addr, username=username, password=password)  # connecting to server
            self.client = client
            return True
        except:
            return False

    def run_command(self, command):
        """
        :param: command: command that you run on the device which you have sshed and already connected by using connect function
        :return: result of the command or message
        """
        try:
            _, ss_stdout, ss_stderr = self.client.exec_command(command)  # executing command on server and return
            # result
            r_out, r_err = ss_stdout.readlines(), ss_stderr.read()  # ss_stderr for error and ss_stdout for
            # result of command
            result = ""  # to save result of the command
            if len(r_err) > 5:
                result = r_err.decode("utf-8")
            else:
                for line in r_out:
                    result = str(result) + str(line)
            # self.client.close()  # closing connection
        except IOError:  # if host/server is not up or for any other issue
            return "host not up", 500
        return result

    def disconnect(self):
        """
        :return: True if the
        """
        try:
            if self.client is not None:
                self.client.close()
                self.client = None
            return True
        except:
            return False
