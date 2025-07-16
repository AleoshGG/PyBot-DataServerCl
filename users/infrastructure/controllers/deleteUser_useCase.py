from flask import jsonify
from users.infrastructure.dependences import getSQLAlchemy
from users.application.useCases.deleteUser_useCase import DeleteUser
from flask_jwt_extended import jwt_required, get_jwt_identity

class DeleteUserController:
    def __init__(self):
        alchemy = getSQLAlchemy()
        self.use_case = DeleteUser(alchemy)
    
    @jwt_required()
    def delete_user(self):
        try:
            user_id = get_jwt_identity()

            if not user_id:
                return jsonify({
                    "status": False,
                    "error": "No se proporcionó ID."
                }), 404

            res = self.use_case.run(user_id)

            if res != True:
                return jsonify({
                "status": False,
                "error": f"No se pudo eliminar el recurso"
                }), 401
            else:
                return jsonify({
                     "status": True,
                     "mensaje": "El recurso se eliminó con éxito",  
                }), 200   
        except Exception as e:
                print(f"Error al ejecutar el caso de uso: {e}")
                return jsonify({
                "status": False,
                "error": f"Error al ejecutar el caso de uso: {e}"
                }), 500  
