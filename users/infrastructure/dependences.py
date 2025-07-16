# users/infrastructure/dependences.py

from users.infrastructure.adapters.SQLALchemy import SQLAlchemy as sql
from users.infrastructure.adapters.Bcrypt import BcryptAdapter

# Variables globales para las dependencias
alchemy = None
bcrypt = None

def goDependencesUsers():
    global alchemy, bcrypt
    alchemy = sql()
    bcrypt = BcryptAdapter()

def getSQLAlchemy():
    return alchemy

def getBcrypt():
    return bcrypt
