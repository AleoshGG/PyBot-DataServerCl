from dataclasses import dataclass
from prototypes.domain.repositories.prototype_repository import IPrototype
from prototypes.domain.models.prototype_model import Prototype
from typing import List

@dataclass
class GetPrototypes:
    def __init__(self, db: IPrototype):
        self.db = db

    def run(self, user_id: int) -> List[Prototype]:
        return self.db.get_protoypes_by_user(user_id)