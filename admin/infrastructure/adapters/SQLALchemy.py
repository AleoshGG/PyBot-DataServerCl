from database.conn.connection import SessionLocal
from admin.domain.models.admin_model import Admin as DomainAdmin
from admin.domain.repositories.admin_repository import IAdmin
from admin.infrastructure.modelsORM.AdminORM import AdminORM
from typing import List
import uuid

class SQLAlchemy(IAdmin):
    def __init__(self):
        self.session = SessionLocal()

    def create_id(self, da: DomainAdmin) -> str:

        object_id = str(uuid.uuid4()).replace('-', '')[:24]
        orm = AdminORM(generated_id=object_id)
        
        self.session.add(orm)
        self.session.commit()
        self.session.refresh(orm)

        return orm.generated_id

    def get_all_ids(self) -> List[str]:
        ids = self.session.query(AdminORM.generated_id).all()
        return [id[0] for id in ids]

    def __del__(self):
        self.session.close()