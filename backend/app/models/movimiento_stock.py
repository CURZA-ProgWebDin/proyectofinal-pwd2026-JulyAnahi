from app.database import db
from app.models.base_model import BaseModel

class MovimientoStock(BaseModel):
    __tablename__ = 'movimientos_stock'
    
    tipo = db.Column(db.String(10), nullable=False) # 'entrada' o 'salida'
    cantidad = db.Column(db.Integer, nullable=False)
    motivo = db.Column(db.String(200), nullable=True)
    
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)