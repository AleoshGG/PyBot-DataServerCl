from users.application.useCases.getUser_useCase import GetUser
from users.infrastructure.dependences import getSQLAlchemy
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

class GetUserController:
    def __init__(self):
        alchemy = getSQLAlchemy()
        self.use_case = GetUser(alchemy)

    @jwt_required()
    def get_user(self):
        try:
            user_id = get_jwt_identity()
            if not user_id:
                return jsonify({
                    "status": False,
                    "error": "No se proporcionó ID."
                }), 404

            user = self.use_case.run(user_id)

            return jsonify({
                "status": True,
                "links": {
			        "self": "http://localhost:8080/work_periods/",
		        },
		        "user": user,  
            }), 200   
        
        except Exception as e:
                print(f"Error al encontrar el recurso {e}")
                return jsonify({
                "status": False,
                "error": f"Error al encontrar el recurso: {e}"
                }), 404
