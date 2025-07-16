
from users.application.useCases.updateUserName_useCase import UpdateUserName
from users.infrastructure.dependences import getSQLAlchemy
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

class UpdateUserNameController:
    def __init__(self):
        alchemy = getSQLAlchemy()
        self.use_case = UpdateUserName(alchemy)
    
    @jwt_required()
    def update_user_name(self, name: str):
        try:
            user_id = get_jwt_identity()

            if not user_id:
                return jsonify({
                    "status": False,
                    "error": "No se proporcionó ID."
                }), 400
            
            if not name or name == "":
                return jsonify({
                    "status": False,
                    "error": "No se proporcionó nombre."
                }), 400


            res = self.use_case.run(user_id, name)

            if res != True:
                return jsonify({
                "status": False,
                "error": f"No se pudo actualizar el recurso"
                }), 401
            else:
                return jsonify({
                     "status": True,
                     "mensaje": "El recurso se actualizó con éxito",  
                }), 200   
        except Exception as e:
                print(f"Error al ejecutar el caso de uso: {e}")
                return jsonify({
                "status": False,
                "error": f"Error al ejecutar el caso de uso: {e}"
                }), 500 