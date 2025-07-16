from flask import Blueprint, request
from users.infrastructure.controllers.createUser_controller import CreateUserController
from users.infrastructure.controllers.deleteUser_useCase import DeleteUserController
from users.infrastructure.controllers.getUser_controller import GetUserController
from users.infrastructure.controllers.signIn_controller import SignInController
from users.infrastructure.controllers.updateUserName_controller import UpdateUserNameController

usersBlueprint = Blueprint('users', __name__)

@usersBlueprint.route('/', methods=['POST'])
def addUser():
    data = request.get_json()
    controller = CreateUserController()
    return controller.createUser(d_body=data)

@usersBlueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    controller = SignInController()
    return controller.signIn(d_body=data)

@usersBlueprint.route('/', methods=['DELETE'])
def deleteUser():
    controller = DeleteUserController()
    return controller.delete_user()

@usersBlueprint.route('/', methods=['GET'])
def getUser():
    controller = GetUserController()
    return controller.get_user()

@usersBlueprint.route('/<string:name>', methods=['PATCH'])
def updateUserName(name):
    controller = UpdateUserNameController()
    return controller.update_user_name(name)