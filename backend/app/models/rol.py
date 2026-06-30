from app.database import db
from app.models.base_model import BaseModel

class Rol(BaseModel):
    __tablename__ = 'roles'

    nombre = db.Column(db.String(50), nullable=False, unique=True)
    users = db.relationship('User', backref='rol', lazy=True)