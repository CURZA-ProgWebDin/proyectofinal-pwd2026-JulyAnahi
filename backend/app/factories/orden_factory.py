from app.models.orden import Orden
from app.models.orden_item import OrdenItem

class OrdenFactory:
    @staticmethod
    def crear_orden(table_number, items_data):

        orden = Orden(table_number=table_number, status='pendiente')
        for item in items_data:
            orden_item = OrdenItem(
                product_id=item['product_id'],
                quantity=item['quantity'],
                unit_price=item['unit_price']
            )
            orden.items.append(orden_item)
        return orden