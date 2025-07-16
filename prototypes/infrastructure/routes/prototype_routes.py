from flask import Blueprint, request
from prototypes.infrastructure.controllers.createPrototype_controller import CreatePrototypeController
from prototypes.infrastructure.controllers.getPrototypes_controller import GetPrototypesController
from prototypes.infrastructure.controllers.updatePrototype_controller import UpdatePrototypeController
from prototypes.infrastructure.controllers.deletePrototype_controller import DeletePrototypeController

prototypesBlueprint = Blueprint('prototypes', __name__)

@prototypesBlueprint.route('/addPrototype', methods=['POST'])
def addPrototype():
    data = request.get_json()
    controller = CreatePrototypeController()
    return controller.createPrototype(d_body=data)

@prototypesBlueprint.route('/list/<int:user_id>', methods=['GET'])
def getPrototypes(user_id):
    controller = GetPrototypesController()
    return controller.getPrototypes(user_id=user_id)

@prototypesBlueprint.route('/<string:prototype_id>', methods=['DELETE'])
def deletePrototype(prototype_id):
    controller = DeletePrototypeController()
    return controller.deletePrototype(prototype_id=prototype_id)

@prototypesBlueprint.route('/<string:prototype_id>', methods=['PUT'])
def updatePrototype(prototype_id):
    data = request.get_json
    controller = UpdatePrototypeController()
    return controller.updatePrototype(prototype_id=prototype_id, d_body= data)