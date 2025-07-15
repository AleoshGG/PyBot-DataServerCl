from abc import ABC, abstractmethod
from admin.domain.models.admin_model import Admin
from typing import List

class IAdmin(ABC):

    @abstractmethod
    def create_id (self, a: Admin) -> str:
        pass


    @abstractmethod
    def get_all_ids (self) -> List[str]:
        pass


