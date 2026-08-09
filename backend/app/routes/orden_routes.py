from flask import Bluprints, request
from app.controllers.orden_controller import OrdenController
from app.decorators.roles import requiere_rol

order_bp = Bluprints('order_bp', __name__)
@order_bp.route('', methods=['POST'])
@order_bp.route('/', methods=['POST'])

def create_order():
    data = request.get_json() or {}
    return OrdenController.create_order(data)

@order_bp.route('/<int:order_id>', methods=['GET'])
def get_order(order_id):
    return OrdenController.get_order(order_id)


@order_bp.route('/kitchen', methods=['GET'])
@requiere_rol('cocina')
def get_kitchen_orders():
    return OrdenController.get_kitchen_orders()

@order_bp.route('<int:order_id>/status',methods=['PUT'])
@requiere_rol('cocina')

def update_order_status(order_id):
    data= request.get_json() or {}
    return OrdenController.update_order_status(order_id, data)

order_bp.route('/cajero', methods=['GET'])
@role_required('cajero')
def get_cashier_orders():
    return OrdenController.get_cashier_orders()

order_bp.route('/<int:order_id>/pagado',methods=['PUT'])
@role_required('cashier')
def pay_order(order_id):
    return OrdenController.pay_order(order_id)

