from abc import ABC, abstractmethod
from users.domain.models.user_model import User

class IUser(ABC):
    
    @abstractmethod
    def create_user(self, u: User) -> int:
        pass

    @abstractmethod
    def signIn(self, email: str) -> User:
        pass

    @abstractmethod
    def get_user(self, user_id: int) -> User:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        pass

    @abstractmethod
    def update_user_name(self, user_id: int, name: str) -> bool:
        pass