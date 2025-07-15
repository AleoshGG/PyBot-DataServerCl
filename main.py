from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from database.conn.connection import engine, SessionLocal
from users.infrastructure.routes.user_routes import usersBlueprint
from users.infrastructure.dependences import db

# Inicializar Flask y SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = engine.url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

db = SQLAlchemy(app)

# Registrar Blueprints
app.register_blueprint(usersBlueprint, url_prefix='/users')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)