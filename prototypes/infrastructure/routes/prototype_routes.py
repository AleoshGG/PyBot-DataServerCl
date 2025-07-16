from flask import Blueprint, request
from prototypes.infrastructure.controllers.createPrototype_controller import CreatePrototypeController
from prototypes.infrastructure.controllers.getPrototypes_controller import GetPrototypesController
from prototypes.infrastructure.controllers.updatePrototype_controller import UpdatePrototypeController
from prototypes.infrastructure.controllers.deletePrototype_controller import DeletePrototypeController

prototypesBlueprint = Blueprint('prototypes', __name__)

@prototypesBlueprint.route('/', methods=['POST'])
def addPrototype():
    data = request.get_json()
    controller = CreatePrototypeController()
    return controller.createPrototype(d_body=data)

@prototypesBlueprint.route('/', methods=['GET'])
def getPrototypes():
    controller = GetPrototypesController()
    return controller.getPrototypes()

@prototypesBlueprint.route('/<string:prototype_id>', methods=['DELETE'])
def deletePrototype(prototype_id):
    controller = DeletePrototypeController()
    return controller.deletePrototype(prototype_id=prototype_id)

@prototypesBlueprint.route('/', methods=['PUT'])
def updatePrototype():
    data = request.get_json()
    controller = UpdatePrototypeController()
    return controller.updatePrototype(d_body=data)