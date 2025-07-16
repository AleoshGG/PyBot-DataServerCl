from flask import jsonify
from prototypes.application.useCases.deletePrototype_useCase import DeletePrototype
from prototypes.infrastructure.dependences import getSQLAlchemy
from flask_jwt_extended import jwt_required

class DeletePrototypeController:
    def __init__(self):
        self.SQLAlchemy = getSQLAlchemy()
        self.use_case = DeletePrototype(db=self.SQLAlchemy)

    @jwt_required()
    def deletePrototype(self, prototype_id: str):
        try:
            if not prototype_id or prototype_id.strip() == "":
                return jsonify({
                    "status": False,
                    "error": "El prototype_id es obligatorio y no debe estar vacío."
                }), 400

            result = self.use_case.run(prototype_id.strip())
            
            if result:
                return jsonify({
                    "status": True,
                    "message": "Prototipo eliminado exitosamente",
                    "data": {
                        "type": "prototypes",
                        "prototype_id": prototype_id
                    }
                }), 200
            else:
                return jsonify({
                    "status": False,
                    "error": "No se encontró el prototipo"
                }), 404

        except Exception as e:
            print(f"Error al eliminar prototipo: {e}")
            return jsonify({
                "status": False,
                "error": f"Error al eliminar prototipo: {e}"
            }), 500