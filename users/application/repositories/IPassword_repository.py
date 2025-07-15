from abc import ABC, abstractmethod

class IPassword(ABC):
    
    @abstractmethod
    def encrypt_password(self, password: str) -> str:
        pass

    @abstractmethod
    def check_password(self, password: str, passwordHash: str) -> bool:
        pass
    