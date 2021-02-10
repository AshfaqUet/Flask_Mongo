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
    os = StringField()

    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "username": self.username,
            "hostname": self.hostname,
            "password": self.password,
            "ssh":  self.ssh,
            "passphrase": self.passphrase,
            "os": self.os
        }