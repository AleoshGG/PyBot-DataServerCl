from users.application.repositories.IPassword_repository import IPassword
from flask_bcrypt import Bcrypt

class BcryptAdapter(IPassword):
    def __init__(self):
        self.bc = Bcrypt()

    def encrypt_password(self, password: str) -> str:
        try: 
            hashed = self.bc.generate_password_hash(password)
            return hashed.decode('utf-8')
        except Exception as e:
            print(f"Ocurrió un error al hashear la contraseña: {e}")
            raise e
        
    def check_password(self, password: str, passwordHash: str) -> bool:
        try:
            return self.bc.check_password_hash(password=password, pw_hash=passwordHash)
        except Exception as e:
            print(f"Error al comparar las contraseñas: {e}")
            raise e