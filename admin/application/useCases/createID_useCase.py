from dataclasses import dataclass
from admin.domain.repositories.admin_repository import IAdmin
from admin.domain.models.admin_model import Admin

@dataclass
class CreateId:
    def __init__(self, db: IAdmin):
        self.db = db


    def run(self, admin: Admin) -> str:
        return self.db.create_id(admin)     