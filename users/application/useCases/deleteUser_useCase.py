from dataclasses import dataclass
from users.domain.repositories.user_repository import IUser

@dataclass
class DeleteUser:
    def __init__(self, db: IUser):
        self.db = db

    def run(self, user_id: int)-> bool:
        return self.db.delete_user(user_id)