from flask import Blueprint
from admin.infrastructure.controllers.createId_controller import CreateIdController
from admin.infrastructure.controllers.getAllids_controller import GetAllIdsController

adminBlueprint = Blueprint('admin', __name__)

@adminBlueprint.route('/create-id', methods=['POST'])
def createId():
    controller = CreateIdController()
    return controller.createId()

@adminBlueprint.route('/ids', methods=['GET'])
def getAllIds():
    controller = GetAllIdsController()
    return controller.getAllIds()