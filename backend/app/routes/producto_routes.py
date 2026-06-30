from flask import Blueprint
from app.controllers.producto_controller import ProductoController
from app.decorators.roles import requiere_rol
from flask_jwt_extended import jwt_required
producto_bp = Blueprint('productos', __name__, url_prefix='/productos')
producto_bp.route('/', methods=['GET'])(jwt_required()(ProductoController.listar))
producto_bp.route('/', methods=['POST'])(requiere_rol('admin')(ProductoController.crear))
producto_bp.route('/<int:id>', methods=['PUT'])(requiere_rol('admin')(ProductoController.editar))
producto_bp.route('/<int:id>', methods=['DELETE'])(requiere_rol('admin')(ProductoController.eliminar))