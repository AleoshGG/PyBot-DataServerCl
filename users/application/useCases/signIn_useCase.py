from dataclasses import dataclass
from users.domain.repositories.user_repository import IUser
from users.domain.models.user_model import User
@dataclass
class SignIn:
    def __init__(self, db: IUser):
        self.db = db
    
    def run(self, email: str) -> User:
        return self.db.signIn(email)
