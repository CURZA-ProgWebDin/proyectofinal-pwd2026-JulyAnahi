from app.database import db
from app.models.base_model import BaseModel

class Categoria(BaseModel):
    __tablename__='categorias'

    nombre = db.Column(db.String(100), nullable=False, unique=True)
    descripcion = db.Column(db.Text, nullable=True)