from users.infrastructure.dependences import db

class UserORM(db.Model):
    __tablename__ = 'users'

    user_id    = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(45),  nullable=False)
    last_name  = db.Column(db.String(45),  nullable=False)    
    email      = db.Column(db.String(100), nullable=False)
    password   = db.Column(db.String(200), nullable=False)