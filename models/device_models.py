from mongoengine import (
    DynamicDocument,
    StringField
)

class Device(DynamicDocument):
    name = StringField()
    username = StringField()
    hostname = StringField(unique=True)
    password = StringField()
    ssh = StringField()
    passphrase = StringField()

    def to_json(self):
        return {
            "name": self.name,
            "username": self.username,
            "hostname": self.hostname,
            "password": self.password,
            "ssh":  self.ssh,
            "passphrase": self.passphrase
        }