from abc import ABC, abstractmethod
from users.domain.models.user_model import User

class IUser(ABC):
    
    @abstractmethod
    def create_user(self, u: User) -> int:
        pass
