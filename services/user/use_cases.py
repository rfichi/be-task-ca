from services.user.entities import User


class UserUseCases:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def create_user(self, user_id: str, name: str):
        user = User(user_id, name)
        return self.user_repo.create(user)

    def get_user(self, user_id: str):
        user = self.user_repo.get_by_id(user_id)
        return user
