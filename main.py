from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from users.infrastructure.routes.user_routes import usersBlueprint
from admin.infrastructure.routes.admin_routes import adminBlueprint
from flask_cors import CORS
from database.conn.connection import engine

# Inicializar Flask y SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = engine.url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

db = SQLAlchemy(app)

# Registrar Blueprints
app.register_blueprint(usersBlueprint, url_prefix='/users')
app.register_blueprint(adminBlueprint, url_prefix='/admin')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1200, debug=True)