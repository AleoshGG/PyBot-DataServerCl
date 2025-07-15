from admin.infrastructure.dependences import db

class AdminORM(db.Model):
    __tablename__ = 'ids'

    generated_id = db.Column(db.String(100), primary_key=True)
    