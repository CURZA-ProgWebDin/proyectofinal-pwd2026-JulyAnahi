from flask import Blueprint, request
from app.controllers.admin_controller import AdminController
from app.decorators.roles import requiere_rol
from app.serializador import generar_url_qr_dinamico

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/users', methods=['GET'])

@requiere_rol('admin')
def get_users():
    return AdminController.get_users()

@admin_bp.route('/users', methods=['POST'])
@requiere_rol('admin')

def create_user():
    data = request.get_json() or {}
    return AdminController.create_user(data)

@admin_bp.route('/users/<int:user_id>',methods = ['PUT'])
@requiere_rol('admin')
def update_user(user_id):
    data = request.get_json() or {}
    return AdminController.update_user(user_id,data)

@admin_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return AdminController.delete_user(user_id)

@admin_bp.route('/mesas/<int:table_number>/activar-qr', methods=['POST'])
@requiere_rol('admin')
def activar_mesa_qr(table_number):
    try:
        url_con_token = generar_url_qr_dinamico(table_number)

        return jsonify({
            'message': f'QR generado para la mesa {table_number}',
            'url_qr':url_con_token
        }), 200
    except Exception as e:
        return jsonify({'msg':'Error al generar el QR', 'error': str(e)}), 500


@admin_bp.route('/products', methods=['GET'])
@requiere_rol('admin')
def get_admin_products():
    return AdminController.get_products()

@admin_bp.route('/products', methods=['POST'])
@requiere_rol('admin')

def update_product(product_id):
    data = request.get_json() or {}
    return AdminController.update_product(product_id, data)

admin_bp.route('/products/<int:product_id>', methods=['DELETE'])
@role_required('admin')
def delete_product(product_id)
    return AdminController.delete_product(product_id)



