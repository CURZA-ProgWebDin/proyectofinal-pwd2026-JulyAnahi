from flask import Blueprint
from app.controllers.producto_controller import ProductoController
from app.decorators.roles import requiere_rol

producto_bp = Blueprint('productos', __name__, url_prefix='/productos')

producto_bp.route('', methods=['GET'])(requiere_rol('admin', 'administrador', 'operador')(ProductoController.listar))
producto_bp.route('', methods=['POST'])(requiere_rol('admin', 'administrador')(ProductoController.crear))
producto_bp.route('/<int:id>', methods=['PUT'])(requiere_rol('admin', 'administrador')(ProductoController.editar))
producto_bp.route('/<int:id>', methods=['DELETE'])(requiere_rol('admin', 'administrador')(ProductoController.eliminar))