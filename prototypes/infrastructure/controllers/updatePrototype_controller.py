from flask import jsonify
from prototypes.application.services.validateId_service import ValidateIdService
from prototypes.application.useCases.updatePrototype_useCase import UpdatePrototype
from prototypes.infrastructure.adapters.Validate import ValidateId
from prototypes.infrastructure.dependences import getSQLAlchemy

class UpdatePrototypeController:
    def __init__(self):
        self.SQLAlchemy = getSQLAlchemy()
        self.use_case = UpdatePrototype(db=self.SQLAlchemy)
        validador = ValidateId()
        self.sValidador = ValidateIdService(validador)

    def updatePrototype(self, prototype_id: str, d_body: dict):
        try:
            if not prototype_id or prototype_id.strip() == "":
                return jsonify({
                    "status": False,
                    "error": "El prototype_id es obligatorio y no debe estar vacío."
                }), 400
            
            try:
                itExist = self.sValidador.run(prototype_id)
                
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

            if not d_body:
                return jsonify({
                    "status": False,
                    "error": "El cuerpo de la petición está vacío."
                }), 400

            new_prototype_name = d_body.get("prototype_name")
            if not new_prototype_name or str(new_prototype_name).strip() == "":
                return jsonify({
                    "status": False,
                    "error": "El campo 'prototype_name' es obligatorio y no debe estar vacío."
                }), 400

            result = self.use_case.run(prototype_id.strip(), new_prototype_name.strip())
            
            if result:
                return jsonify({
                    "status": True,
                    "message": "Prototipo actualizado exitosamente",
                    "data": {
                        "type": "prototypes",
                        "prototype_id": prototype_id,
                        "attributes": {
                            "prototype_name": new_prototype_name.strip()
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