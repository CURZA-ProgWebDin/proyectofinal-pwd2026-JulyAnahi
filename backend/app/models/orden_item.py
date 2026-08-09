from app.database import db
from app.models.base_model import BaseModel

class OrdenItem(BaseModel):
    __tablename__ = 'ordenes_items'

    order_id= db.Column(db.Integer, db.ForeignKey('ordenes.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable= False)
    unit_price = db.Column(db.Float, nullable=False)

    # relacion con la tabla de productos para traer el nombre del producto en el diccionario
    product = db.relationship('Producto', lazy=True)

    def to_dict(self):

        data = super().to_dict()

        data['subtotal'] = self.quantity * self.unit_price

        data['product_name'] = self.product.name if self.product else 'Producto desconocido' 

        return data
    
    # def to_dict(self):
    #     return{
    #         'id':self.id,
    #         'order_id': self.order_id,
    #         'product_id':self.product_id,
    #         'product_name':self.product.name if self.product else 'Producto desconocido',
    #         'quantity':self.quantity,
    #         'unit_price':self.unit_price,
    #         'subtotal':self.quantity * self.unit_price
    #     }


