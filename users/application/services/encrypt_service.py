from dataclasses import dataclass
from users.application.repositories.IPassword_repository import IPassword

@dataclass
class EncryptPasswordService:
    def __init__(self, encrypt: IPassword):
        self.encrypt = encrypt

    def run(self, password: str) -> str:
        return self.encrypt.encrypt_password(password=password)
        