# prototypes/infrastructure/dependences.py

from prototypes.infrastructure.adapters.SQLAlchemy import PrototypeSQLAlchemy

# Variables globales para las dependencias
alchemy = None

def goDependencesPrototypes():
    global alchemy
    alchemy = PrototypeSQLAlchemy()

def getSQLAlchemy():
    return alchemy