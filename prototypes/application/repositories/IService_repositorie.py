from abc import ABC, abstractmethod

class IService(ABC):
    @abstractmethod
    def itExist(self, id: str) -> bool:
        pass