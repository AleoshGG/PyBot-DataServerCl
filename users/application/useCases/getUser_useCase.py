from dataclasses import dataclass
from users.domain.repositories.user_repository import IUser
from users.domain.models.user_model import User

@dataclass
class GetUser:
    def __init__(self, db: IUser):
        self.db = db

    def run(self, user_id: int)-> User:
        return self.db.get_user(user_id)