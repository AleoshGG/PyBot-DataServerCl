from flask import jsonify
from prototypes.application.useCases.getPrototypes_useCase import GetPrototypes
from prototypes.infrastructure.dependences import getSQLAlchemy
from flask_jwt_extended import jwt_required, get_jwt_identity

class GetPrototypesController:
    def __init__(self):
        self.SQLAlchemy = getSQLAlchemy()
        self.use_case = GetPrototypes(db=self.SQLAlchemy)

    @jwt_required()
    def getPrototypes(self):
        try:
            user_id = get_jwt_identity()
            if not user_id:
                return jsonify({
                    "status": False,
                    "error": "No se proporcionó ID."
                }), 404

            prototypes = self.use_case.run(user_id)
            
            prototypes_data = []
            for prototype in prototypes:
                prototypes_data.append({
                    "prototype_id": prototype.prototype_id,
                    "prototype_name": prototype.prototype_name,
                    "model": prototype.model,
                    "user_id": prototype.user_id
                })

            return jsonify({
                "status": True,
                "data": {
                    "type": "prototypes",
                    "count": len(prototypes_data),
                    "prototypes": prototypes_data
                }
            }), 200

        except Exception as e:
            print(f"Error al obtener prototipos: {e}")
            return jsonify({
                "status": False,
                "error": f"Error al obtener prototipos: {e}"
            }), 500