from dataclasses import dataclass

from prototypes.application.repositories.IService_repositorie import IService

@dataclass 
class ValidateIdService:
    def __init__(self, s: IService):
        self.service = s

    def run(self, id: str)-> bool:
        return self.service.itExist(id)