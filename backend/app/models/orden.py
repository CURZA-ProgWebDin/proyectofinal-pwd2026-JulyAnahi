from app.database import db
from app.models.base_model import BaseModel

class Orden(BaseModel):
    __tablename__ = 'ordenes'

    table_number = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default='pendiente', nullable=False)# van a ser pendiente, preparando, listo , pagado

    items = db.relationship('OrdenItem', backref='orden', lazy=True, cascade='all, delete-orphan')
    #item1 = OrdenItem(product_id=1, quantity=2, unit_price=10.0)

    def to_dict(self):
        data = super().to_dict()

        data['items'] = [item.to_dict() for item in self.items]

        return data

    # def to_dict(self):
    #     return {
    #         'id':self.id,
    #         'table_number': self.table_number,
    #         'status': self.status,
    #         'created_at': self.created_at.isoformat(),
    #         'updated_at': self.updated_at.isoformat(),
    #         'items': [item.to_dict() for item in self.item]
    #     }
    

