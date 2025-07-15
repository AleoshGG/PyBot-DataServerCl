# admin/infrastructure/dependences.py
from admin.infrastructure.adapters.SQLAlchemy import SQLAlchemy as sql

# Variables globales para las dependencias
alchemy = None
bcrypt = None

def goDependencesAdmin():
    global alchemy
    alchemy = sql()

def getSQLAlchemy():
    return alchemy