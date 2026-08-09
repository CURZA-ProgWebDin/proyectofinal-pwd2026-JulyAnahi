from app.database import db
from app.models.base_model import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(BaseModel):
    __tablename__ = 'usuarios'

    username = db.Column(db.String(50), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(25), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    _hidden_fields = ['password_hash']

    # def to_dict(self):
    #     return{
    #         'id': self.id,
    #         'username': self.username,
    #         'role': self.role
    #     }