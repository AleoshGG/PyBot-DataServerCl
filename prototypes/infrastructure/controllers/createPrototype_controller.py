from flask import jsonify
from prototypes.application.services.validateId_service import ValidateIdService
from prototypes.application.useCases.createProtoype_useCase import CreatePrototype
from prototypes.domain.models.prototype_model import Prototype
from prototypes.infrastructure.adapters.Validate import ValidateId
from prototypes.infrastructure.dependences import getSQLAlchemy
from flask_jwt_extended import jwt_required, get_jwt_identity

class CreatePrototypeController:
    def __init__(self):
        self.SQLAlchemy = getSQLAlchemy()
        self.use_case = CreatePrototype(db=self.SQLAlchemy)
        validador = ValidateId()
        self.sValidador = ValidateIdService(validador)

    @jwt_required()
    def createPrototype(self, d_body: dict):
        try:
            if not d_body:
                return jsonify({
                    "status": False,
                    "error": "El cuerpo de la petición está vacío."
                }), 400

            required_fields = ["prototype_id", "prototype_name"]
            for field in required_fields:
                value = d_body.get(field)
                if not value or str(value).strip() == "":
                    return jsonify({
                        "status": False,
                        "error": f"El campo '{field}' es obligatorio y no debe estar vacío."
                    }), 400

            user_id = get_jwt_identity()
            if not user_id:
                return jsonify({
                    "status": False,
                    "error": "No se proporcionó ID."
                }), 404
            
            prototype = Prototype(
                d_body.get("prototype_id").strip(),
                d_body.get("prototype_name").strip(),
                "default",  # model por defecto
                user_id
            )
        except Exception as e:
            print(f"Error al obtener datos del cuerpo del body: {e}")
            return jsonify({
                "status": False,
                "error": f"Error al obtener datos del cuerpo del body: {e}"
            }), 400

        try:
            itExist = self.sValidador.run(prototype.prototype_id)
            
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

        try: 
            prototype_id = self.use_case.run(prototype)
        except Exception as e:
            print(f"Error al crear el prototipo: {e}")
            return jsonify({
                "status": False,
                "error": f"Error al crear el prototipo: {e}"
            }), 500

        return jsonify({
            "status": True,
            "data": {
                "type": "prototypes",
                "prototype_id": prototype_id,
                "attributes": {
                    "prototype_name": prototype.prototype_name,
                    "model": prototype.model,
                    "user_id": prototype.user_id
                },
            },
        }), 201