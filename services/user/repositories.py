class UserRepo:
    def __init__(self):
        self.users = {}

    def create(self, user):
        if not self.users.get(user.user_id):
            self.users[user.user_id] = user
            return user
        return None

    def get_by_id(self, user_id):
        return self.users.get(user_id)
