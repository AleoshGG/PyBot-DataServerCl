from flask import Blueprint, request
from users.infrastructure.controllers.createUser_controller import CreateUserController

usersBlueprint = Blueprint('users', __name__)

@usersBlueprint.route('/add', methods=['POST'])
def addUser():
    data = request.get_json()
    controller = CreateUserController()
    return controller.createUser(d_body=data)
