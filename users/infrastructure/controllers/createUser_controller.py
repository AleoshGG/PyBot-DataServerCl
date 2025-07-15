from flask import jsonify
from users.application.useCases.createUser_useCase import CreateUser
from users.infrastructure.adapters.SQLAlchemy import SQLAlchemy
from users.domain.models.user_model import User
from users.application.services.encrypt_service import EncryptPasswordService
from users.infrastructure.adapters.Bcrypt import BcryptAdapter
class CreateUserController:
    def __init__(self):
        self.SQLAlchemy = SQLAlchemy()
        self.use_case = CreateUser(db=self.SQLAlchemy)
        bcypt = BcryptAdapter()
        self.service_encrypt = EncryptPasswordService(bcypt)

    def createUser(self, d_body: dict):
        try:
            if not d_body:
                return jsonify({
                    "status": False,
                    "error": "El cuerpo de la petición está vacío."
                }), 400

            required_fields = ["email", "password", "first_name", "last_name"]
            for field in required_fields:
                value = d_body.get(field)
                if not value or str(value).strip() == "":
                    return jsonify({
                        "status": False,
                        "error": f"El campo '{field}' es obligatorio y no debe estar vacío."
                    }), 400

            user = User(
                0,
                d_body.get("first_name").strip(),
                d_body.get("last_name").strip(),
                d_body.get("email").strip(),
                d_body.get("password").strip()
            )
        except Exception as e:
            print(f"Error al obtener datos del cuerpo del body: {e}")
            return jsonify({
                "status": False,
                "error": f"Error al obtener datos del cuerpo del body: {e}"
            }), 400

        try:
            pw_hash = self.service_encrypt.run(user.password)
            user.password = pw_hash
        except Exception as e:
            print(f"Error en el servicio de encriptación: {e}")
            return jsonify({
            "status": False,
            "error": f"Error en el servicio de encriptación: {e}"
             }), 500

        try: 
            id = self.use_case.run(user)
        except Exception as e:
            print(f"Error al crear el recurso: {e}")
            return jsonify({
            "status": False,
            "error": f"Error al crear el recurso: {e}"
             }), 500

        return jsonify({
            "status": True,
		    "data": {
                "type": "users",
                "user_id": id,
                "attributes": {
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name
                },
		    },
        }), 201
