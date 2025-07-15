from flask import jsonify
from admin.application.useCases.GetAllids_useCase import GetAllids
from admin.infrastructure.dependences import getSQLAlchemy

class GetAllIdsController:
    def __init__(self):
        self.SQLAlchemy = getSQLAlchemy()
        self.use_case = GetAllids(db=self.SQLAlchemy)

    def getAllIds(self):
        try:
            ids = self.use_case.run()
        except Exception as e:
            print(f"Error al obtener los IDs: {e}")
            return jsonify({
                "status": False,
                "error": f"Error al obtener los IDs: {e}"
            }), 500

        return jsonify({
            "status": True,
            "data": {
                "type": "admin",
                "attributes": {
                    "ids": ids,
                    "total": len(ids)
                }
            }
        }), 200