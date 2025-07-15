from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from users.infrastructure.routes.user_routes import usersBlueprint
from admin.infrastructure.routes.admin_routes import adminBlueprint
from database.conn.connection import engine, SessionLocal
from users.infrastructure.dependences import db

# Inicializar Flask y SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = engine.url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Registrar Blueprints
app.register_blueprint(usersBlueprint, url_prefix='/users')
app.register_blueprint(adminBlueprint, url_prefix='/admin')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1200, debug=True)