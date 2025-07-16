from database.db import db

class PrototypeORM(db.Model):
    __tablename__ = 'prototypes'

    prototype_id   = db.Column(db.String(100), primary_key=True)
    prototype_name = db.Column(db.String(45),  nullable=False)
    model          = db.Column(db.String(45),  nullable=False)
    user_id        = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)  # Cambiar a 'users.user_id'

    # Relación con usuarios
    user = db.relationship('UserORM', backref='prototypes')