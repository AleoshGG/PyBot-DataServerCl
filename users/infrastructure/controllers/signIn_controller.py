from datetime import timedelta
from flask import jsonify
from users.domain.models.user_model import User
from users.infrastructure.dependences import getBcrypt, getSQLAlchemy
from users.application.services.checkPassword_service import CheckPasswordServiece
from users.application.useCases.signIn_useCase import SignIn
from flask_jwt_extended import create_access_token

class SignInController:
    def __init__(self):
        alchemy = getSQLAlchemy()
        bcrypt = getBcrypt()
        self.use_case = SignIn(alchemy)
        self.service = CheckPasswordServiece(bcrypt)

    def signIn(self, d_body: dict):
        try:    
            if not d_body:
                return jsonify({
                    "status": False,
                    "error": "El cuerpo de la petición está vacío."
                }), 400

            required_fields = ["email", "password"]
            for field in required_fields:
                value = d_body.get(field)
                if not value or str(value).strip() == "":
                    return jsonify({
                        "status": False,
                        "error": f"El campo '{field}' es obligatorio y no debe estar vacío."
                    }), 400    

            user = User(
                0,
                "",
                "",
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
            userF = self.use_case.run(user.email)
        except Exception as e:
                print(f"Error al hacer el get: {e}")
                return jsonify({
                "status": False,
                "error": f"No se encontró el recurso: {e}"
        }), 404

        try:
            isMatched = self.service.run(password=user.password, passwordHash=userF.password)

            if (isMatched != True):    
                return jsonify({
                "status": False,
                "error": f"Las contraseñas son incorrectas"
                }), 401
            else:
                expires = timedelta(hours=5)
                access_token = create_access_token(identity=str(userF.user_id), expires_delta=expires)
                return jsonify({
                     "mensaje": "Inicio de sesión exitoso", 
                     "access_token": access_token,
                     "status": True
                }), 200

        except Exception as e:
                print(f"Error en el servicio de verificaión: {e}")
                return jsonify({
                "status": False,
                "error": f"Error en el servicio de verificaión: {e}"
                }), 500
