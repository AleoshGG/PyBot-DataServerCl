from dataclasses import dataclass
from users.application.repositories.IPassword_repository import IPassword

@dataclass
class CheckPasswordServiece:
    def __init__(self, check: IPassword):
        self.check = check

    def run(self, password: str, passwordHash: str) -> bool:
        return self.check.check_password(password=password, passwordHash=passwordHash)
