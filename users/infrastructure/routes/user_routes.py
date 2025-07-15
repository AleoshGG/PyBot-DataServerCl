from flask import Blueprint, request
from users.infrastructure.controllers.createUser_controller import CreateUserController
from users.infrastructure.controllers.signIn_controller import SignInController


usersBlueprint = Blueprint('users', __name__)

@usersBlueprint.route('/add', methods=['POST'])
def addUser():
    data = request.get_json()
    controller = CreateUserController()
    return controller.createUser(d_body=data)

@usersBlueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    controller = SignInController()
    return controller.signIn(d_body=data)
