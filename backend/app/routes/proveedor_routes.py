from flask import Blueprint
from app.controllers.proveedor_controller import ProveedorController
from app.decorators.roles import requiere_rol
proveedor_bp = Blueprint('proveedores', __name__, url_prefix='/proveedores')
proveedor_bp.route('/', methods=['GET'])(requiere_rol('admin')(ProveedorController.listar))
proveedor_bp.route('/', methods=['POST'])(requiere_rol('admin')(ProveedorController.crear))
proveedor_bp.route('/<int:id>', methods=['PUT'])(requiere_rol('admin')(ProveedorController.editar))
proveedor_bp.route('/<int:id>', methods=['DELETE'])(requiere_rol('admin')(ProveedorController.eliminar))