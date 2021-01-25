from app import db


class User(db.Document):
    name = db.StringField()
    email = db.StringField()

    def to_json(self):
        return {
            "name": self.name,
            "email": self.email
        }


class Device(db.Document):
    name = db.StringField()
    username = db.StringField()
    hostname = db.StringField()
    password = db.StringField()
    ssh = db.StringField(unique=True)
    passphrase = db.StringField()

    def to_json(self):
        return {
            "name": self.name,
            "username": self.username,
            "hostname": self.hostname,
            "password": self.password,
            "ssh-key":  self.ssh,
            "passphrase": self.passphrase
        }
