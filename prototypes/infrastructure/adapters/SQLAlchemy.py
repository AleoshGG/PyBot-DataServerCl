from database.conn.connection import SessionLocal
from prototypes.domain.models.prototype_model import Prototype as DomainPrototype
from prototypes.domain.repositories.prototype_repository import IPrototype
from prototypes.infrastructure.modelsORM.PrototypeORM import PrototypeORM
from typing import List

class PrototypeSQLAlchemy(IPrototype):
    def __init__(self):
        self.session = SessionLocal()

    def create_prototype(self, dp: DomainPrototype) -> str:
        try: 
            orm = PrototypeORM(
                prototype_id   = dp.prototype_id,
                prototype_name = dp.prototype_name,
                model          = dp.model,
                user_id        = dp.user_id
            )
            
            self.session.add(orm)
            self.session.commit()
            self.session.refresh(orm)

            return orm.prototype_id
        except Exception as e:
            self.session.rollback()
            print(f"Error al insertar prototipo con SQLAlchemy: {e}")
            raise e

    def get_prototypes_by_user(self, user_id: int) -> List[DomainPrototype]:
        try:
            prototypes = PrototypeORM.query.filter(PrototypeORM.user_id == user_id).all()
            
            domain_prototypes = []
            for p in prototypes:
                domain_prototype = DomainPrototype(
                    p.prototype_id,
                    p.prototype_name,
                    p.model,
                    p.user_id
                )
                domain_prototypes.append(domain_prototype)

            return domain_prototypes
        except Exception as e:
            print(f"Error al obtener prototipos: {e}")
            raise e

    def delete_prototype(self, prototype_id: str) -> bool:
        try:
            prototype = self.session.get(PrototypeORM, prototype_id)
            
            if prototype is None:
                return False
    
            self.session.delete(prototype)
            self.session.commit()
            return True
        
        except Exception as e:
            self.session.rollback()
            print(f"Error al eliminar prototipo: {e}")
            raise e

    def update_prototype(self, prototype_id: str, new_prototype_name: str, new_id: str) -> bool:
        try:
            # 1) Carga con la misma sesión
            p = self.session.get(PrototypeORM, prototype_id)  
            if p is None:
                return False

            # 2) Modifica
            p.prototype_id = new_id
            p.prototype_name = new_prototype_name

            # 3) Commit sobre self.session
            self.session.commit()
            return True

        except Exception:
            self.session.rollback()
            raise
        finally:
            self.session.close()

    def __del__(self):
        self.session.close()