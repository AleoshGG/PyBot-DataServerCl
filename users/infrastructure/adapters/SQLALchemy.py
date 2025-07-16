from database.conn.connection import SessionLocal
from users.domain.models.user_model import User as DomainUser
from users.domain.repositories.user_repository import IUser
from users.infrastructure.modelsORM.UserORM import UserORM

class SQLAlchemy(IUser):
    def __init__(self):
        self.session = SessionLocal()

    def create_user(self, du: DomainUser) -> int:
        try: 
            orm = UserORM(
                first_name = du.first_name,
                last_name  = du.last_name,
                email      = du.email,
                password   = du.password
                )
            
            self.session.add(orm)
            self.session.commit()
            self.session.refresh(orm)

            return orm.user_id
        except Exception as e:
            print(f"Error al insertar con SQLAlchemy: {e}")
            raise e

    def signIn(self, email: str) -> DomainUser:
        try:
            u = UserORM.query.filter(UserORM.email == email).first()

            du_user = DomainUser(
                u.user_id,
                u.first_name,
                u.last_name,
                u.email,
                u.password   
            )

            return du_user
        except Exception as e:
            print(f"Error al obtener el recurso: {e}")
            raise e

    def get_user(self, user_id: int) -> DomainUser:
        try:
            u = UserORM.query.get(user_id)
            
            du_user = DomainUser(
                u.user_id,
                u.first_name,
                u.last_name,
                u.email,
                ""   
            )

            return du_user
        except Exception as e:
            print(f"Error al obtener el recurso por el ID: {e}")
            raise e
            
    def delete_user(self, user_id: int) -> bool:
        try:
            u = self.session.get(UserORM, user_id)  
            if u is None:
                return False
            
            self.session.delete(u)
            self.session.commit()
            return True

        except Exception:
            self.session.rollback()
            raise
        finally:
            self.session.close()
    
    def update_user_name(self, user_id: int, name: str) -> bool:
        try:
            # 1) Carga con la misma sesión
            u = self.session.get(UserORM, user_id)  
            if u is None:
                return False

            # 2) Modifica
            u.first_name = name

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