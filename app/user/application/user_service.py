from ulid import ULID
from datetime import datetime
from utils.crypto import Crypto

from user.domain.user import User
from user.domain.repository.user_repo import IUserRepository
from user.infra.repository.user_repo import UserRepository

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.ulid = ULID()
        self.crypto = Crypto()

    def create_user(self, name: str, email: str, password: str):
        now = datetime.now()
        user: User = User(
            id=self.ulid.generate(),
            name=name,
            email=email,
            password=self.crypto.encrypt(password),
            created_at=now,
            updated_at=now,
        )
        self.user_repository.save(user)
        return user
    
    def get_user_by_id(self, id: str):
        return self.user_repository.find_by_id(id)