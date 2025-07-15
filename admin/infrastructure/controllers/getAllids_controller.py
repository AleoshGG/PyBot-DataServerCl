from flask import jsonify
from admin.application.useCases.GetAllids_useCase import GetAllids
from admin.infrastructure.adapters.SQLALchemy import SQLAlchemy

class GetAllIdsController:
    def __init__(self):
        self.SQLAlchemy = SQLAlchemy()
        self.use_case = GetAllids(db=self.SQLAlchemy)

    def getAllIds(self):
        ids = self.use_case.run()
        
        return jsonify({
            "msg": "Success",
            "ids": ids
        }), 200