from dataclasses import dataclass
from admin.domain.repositories.admin_repository import IAdmin
from typing import List

@dataclass
class GetAllids:
    def __init__(self, db:IAdmin):
        self.db = db

    def run(self) -> List[str]:
        return self.db.get_all_ids()    