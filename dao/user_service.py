import logging
from models.user_models import User

logger = logging.getLogger("dao.device_service")

class UserService:
    def __init__(self):
        self.users = User
        self.users_list = list()

    def get_user(self, email):
        user = User.objects(email=email).first()
        if not user:
            return {'error': 'data not found'}
        else:
            return user.to_json()

    def get_all_users(self):
        self.Users_list = User.objects().all()
        if not self.Users_list:
            return {'error': 'data not found'}
        else:
            return self.Users_list

    def add_new_user(self,user_info):
        self.users = User(
            name=user_info['name'],
            email=user_info['email']
        )
        self.users.save()
        return self.users.to_json()

    def update_user(self, user_info):
        self.users = User.objects(email=user_info['email']).first()
        if not self.users:
            return {'error': 'device not found'}
        else:
            self.users.update(name=user_info["name"])
        return self.get_user(self.users['email'])

    def delete_user(self,user_info):
        self.users = User.objects(email=user_info['email']).first()
        if not self.users:
            return {'error': 'data not found'}
        else:
            self.users.delete()
        return self.users.to_json()
