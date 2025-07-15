from flask import jsonify
from admin.application.useCases.createID_useCase import CreateId
from admin.infrastructure.adapters.SQLAlchemy import SQLAlchemy
from admin.domain.models.admin_model import Admin

class CreateIdController:
    def __init__(self):
        self.SQLAlchemy = SQLAlchemy()
        self.use_case = CreateId(db=self.SQLAlchemy)

    def createId(self):
        try:
            admin = Admin(generated_id="")  # Se generará en el adaptador
        except Exception as e:
            print(f"Error al crear el modelo Admin: {e}")
            return jsonify({
                "status": False,
                "error": f"Error al crear el modelo Admin: {e}"
            }), 400

        try:
            generated_id = self.use_case.run(admin)
        except Exception as e:
            print(f"Error al crear el recurso: {e}")
            return jsonify({
                "status": False,
                "error": f"Error al crear el recurso: {e}"
            }), 500

        return jsonify({
            "status": True,
            "data": {
                "type": "admin",
                "attributes": {
                    "objectID": generated_id
                }
            }
        }), 201