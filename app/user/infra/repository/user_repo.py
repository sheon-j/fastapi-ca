from user.domain.repository.user_repo import IUserRepository

class UserRepository(IUserRepository):
    def save(self, user: User):
        pass