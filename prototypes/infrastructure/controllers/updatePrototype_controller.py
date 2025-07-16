from flask import jsonify
from prototypes.application.services.validateId_service import ValidateIdService
from prototypes.application.useCases.updatePrototype_useCase import UpdatePrototype
from prototypes.infrastructure.adapters.Validate import ValidateId
from prototypes.infrastructure.dependences import getSQLAlchemy
from flask_jwt_extended import jwt_required

class UpdatePrototypeController:
    def __init__(self):
        self.SQLAlchemy = getSQLAlchemy()
        self.use_case = UpdatePrototype(db=self.SQLAlchemy)
        validador = ValidateId()
        self.sValidador = ValidateIdService(validador)

    @jwt_required()
    def updatePrototype(self, d_body: dict):
        try:
            print(d_body)
            if not d_body:
                return jsonify({
                    "status": False,
                    "error": "El cuerpo de la petición está vacío."
                }), 400

            required_fields = ["prototype_id", "new_name", "new_id"]
            for field in required_fields:
                value = d_body.get(field)
                if not value or str(value).strip() == "":
                    return jsonify({
                        "status": False,
                        "error": f"El campo '{field}' es obligatorio y no debe estar vacío."
                    }), 400
                
            prototype_id = d_body.get("prototype_id")
            new_name = d_body.get("new_name")
            new_id = d_body.get("new_id")
            
            try:
                itExist = self.sValidador.run(new_id)
                
                if itExist == False:
                    return jsonify({
                        "status": False,
                        "error": "El Id no es válido."
                    }), 400
            except Exception as e:
                return jsonify({
                    "status": False,
                    "error": f"Error al validar el ID: {e}."
                }), 5000

            result = self.use_case.run(prototype_id, new_name, new_id)
            
            if result:
                return jsonify({
                    "status": True,
                    "message": "Prototipo actualizado exitosamente",
                    "data": {
                        "type": "prototypes",
                        "prototype_id": d_body.get("new_id"),
                        "attributes": {
                            "prototype_name": d_body.get("new_name")
                        }
                    }
                }), 200
            else:
                return jsonify({
                    "status": False,
                    "error": "No se encontró el prototipo"
                }), 404

        except Exception as e:
            print(f"Error al actualizar prototipo: {e}")
            return jsonify({
                "status": False,
                "error": f"Error al actualizar prototipo: {e}"
            }), 500