from dataclasses import dataclass
from users.domain.repositories.user_repository import IUser
from users.domain.models.user_model import User

@dataclass
class CreateUser:
    def __init__(self, db: IUser):
        self.db = db

    
    def run(self, user: User) -> int:
        return self.db.create_user(user)
