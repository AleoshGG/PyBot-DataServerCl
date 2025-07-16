from dataclasses import dataclass
from users.domain.repositories.user_repository import IUser

@dataclass
class UpdateUserName:
    def __init__(self, db: IUser):
        self.db = db

    def run(self, user_id: int, name: str) -> bool:
        return self.db.update_user_name(user_id, name)