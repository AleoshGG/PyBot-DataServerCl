from abc import ABC, abstractmethod
from prototypes.domain.models.prototype_model import Prototype
from typing import List

class IPrototype(ABC):

    @abstractmethod
    def create_prototype(self, p: Prototype) -> int:
        pass

    @abstractmethod
    def get_prototypes_by_user(self, user_id: int) -> List[Prototype]:
        pass

    @abstractmethod
    def delete_prototype(self, prototype_id: int) -> int:
        pass

    @abstractmethod
    def update_prototype(self, prototype_id: str, new_prototype_name: str) -> bool:
        pass