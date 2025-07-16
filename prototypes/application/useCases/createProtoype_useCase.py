from dataclasses import dataclass
from prototypes.domain.repositories.prototype_repository import IPrototype
from prototypes.domain.models.prototype_model import Prototype

@dataclass
class CreatePrototype:
    def __init__(self, db: IPrototype):
        self.db = db

    def run(self, prototype: Prototype) -> str:
        return self.db.create_prototype(prototype)