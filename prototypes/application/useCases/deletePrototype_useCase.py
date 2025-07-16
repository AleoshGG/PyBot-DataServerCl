from dataclasses import dataclass
from prototypes.domain.repositories.prototype_repository import IPrototype

@dataclass
class DeletePrototype:
    def __init__(self, db: IPrototype):
        self.db = db

    def run(self, prototype_id: str) -> bool:
        return self.db.delete_protoype(prototype_id)