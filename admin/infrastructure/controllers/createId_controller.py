from flask import jsonify
from admin.application.useCases.createID_useCase import CreateId
from admin.infrastructure.adapters.SQLALchemy import SQLAlchemy
from admin.domain.models.admin_model import Admin

class CreateIdController:
    def __init__(self):
        self.SQLAlchemy = SQLAlchemy()
        self.use_case = CreateId(db=self.SQLAlchemy)

    def createId(self):
        admin = Admin(generated_id="")  # Se generará en el adaptador
        
        generated_id = self.use_case.run(admin)
        
        return jsonify({
            "msg": "Success",
            "objectID": generated_id
        }), 201