from flask import jsonify , current_app
from app.database import db
from app.models.orden import Orden
from app.models.producto import Producto
from app.factories.orden_factory import OrdenFactory
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
class OrdenController:
    @staticmethod
    def create_order(data):
        token_qr = data.get('token_qr')
        table_number = data.get('table_number')
        items = data.get('items')

        if not table_number or not items or not isinstance(items, list) or len(items) == 0:
            return jsonify({'msg':'el numero de la mesa y los items son requeridos'}), 400
        

        if not token_qr:
            return jsonify({'msg':'Qr invalido'}), 400
     
        serializador = URLSafeTimedSerializer(current_app.config['SECRET_Key'])

        try:
            datos_encriptados= serializador.loads(token_qr, max_age=60)

            if datos_encriptados.get('table_number') != table_number:
                return jsonify({'msg':'El QR no pertenece a esta mesa'}), 403    

        except SignatureExpired:
            return jsonify({'msg':'codigo QR expirado'}), 403
        except BadSignature:
            return jsonify({'msg':'Codigo QR invalido o alterado'}), 403
        
       
        items_data = []
        for item in items:
            product_id = item.get('product_id')
            quantity =item.get('quantity')

            if not product_id or not quantity or quantity <= 0:
                return jsonify({'msg':'Los items enviados son invalidos'}), 400

            product = Producto.query.get(product_id)
            if not product:
                return jsonify({'msg':f'El producto con el id {product_id} no existe'}), 404

            if not product.is_available:
                return jsonify({'msg':f'El producto {product.name} no esta disponible'}), 400

            items_data.append({
                'product_id': product_id,
                'quantity' : quantity,
                'unit_price': product.price   
            })

        order = OrdenFactory.crear_orden(table_number,items_data)
        db.session.add(order)
        db.session.commit()

        return jsonify(order.to_dict()), 201

    @staticmethod
    def get_order(order_id):
        order = Orden.query.get(order_id)
        if not order:
            return jsonify({'msg':'Orden no encontrada o no existe'}), 404
        return jsonify({order.to_dict()}), 200

    @staticmethod
    def get_kitchen_orders():
        orders = Orden.query.filter(Orden.status.in_(['pendiente', 'preparando','lista', 'pagada' ]))
        return jsonify([order.to_dict() for order in orders]), 200

    @staticmethod
    def update_order_status(order_id, data):

        status = data.get('status')

        if not status or status not in['pendiente', 'preparando', 'lista', 'pagado']:
            return jsonify({'msg':'Sin estado o estado invalido'}), 400

        order = Orden.query.get(order_id)

        if not order:
            return jsonify({'msg':'orden no encontrada'}), 404

        order.status = status
        db.session.commit()
        return jsonify(order.to_dict()), 200

    @staticmethod
    def get_cashier_orders():

        orders = Orden.query.filter(Orden.status.in_(['pendiente', 'preparando', 'lista'])).order_by(Orden.created_at.desc()).all()

        return jsonify(order.to_dict() for order in orders), 200

    @staticmethod
    def pay_order(order_id):

        order = Orden.query.get(order_id)

        if not order:
            return jsonify({'msg':'Orden no encontrada'}), 404
        order.status = 'paid'
        db.session.commit()
        return jsonify(order.to_dict()), 200
