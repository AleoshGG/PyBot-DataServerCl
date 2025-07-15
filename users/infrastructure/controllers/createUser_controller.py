from flask import jsonify
from users.application.useCases.createUser_useCase import CreateUser
from users.infrastructure.adapters.SQLALchemy import SQLAlchemy
from users.domain.models.user_model import User

class CreateUserController:
    def __init__(self):
        self.SQLAlchemy = SQLAlchemy()
        self.use_case = CreateUser(db=self.SQLAlchemy)

    def createUser(self, d_body: dict):
        user = User(
            0, 
            d_body.get("first_name"),
            d_body.get("last_name"),
            d_body.get("email"),
            d_body.get("password")
        )

        id = self.use_case.run(user)
        
        return jsonify({
            "msg": "Success",
            "user_id": id
        }), 201
