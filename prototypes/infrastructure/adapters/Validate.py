
from admin.infrastructure.modelsORM.AdminORM import AdminORM
from database.conn.connection import SessionLocal
from prototypes.application.repositories.IService_repositorie import IService


class ValidateId(IService):
    def __init__(self):
        self.session = SessionLocal()

    def itExist(self, id: str) -> bool:
        try:
            u = AdminORM.query.filter(AdminORM.generated_id == id).first()

            if not u:
                return False
            
            return True
        except Exception as e:
            print(f"Error al obtener el recurso: {e}")
            raise e