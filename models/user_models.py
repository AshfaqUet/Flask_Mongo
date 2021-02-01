from mongoengine import (
    DynamicDocument,
    StringField
)

class User(DynamicDocument):
    name = StringField()
    email = StringField(unique=True)

    def to_json(self):
        return {
            "name": self.name,
            "email": self.email
        }



