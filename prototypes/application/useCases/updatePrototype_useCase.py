from dataclasses import dataclass
from prototypes.domain.repositories.prototype_repository import IPrototype

@dataclass
class UpdatePrototype:
    def __init__(self, db: IPrototype):
        self.db = db

    def run(self, prototype_id: str, new_prototype_name: str, new_id: str) -> bool:
        return self.db.update_prototype(prototype_id, new_prototype_name, new_id)