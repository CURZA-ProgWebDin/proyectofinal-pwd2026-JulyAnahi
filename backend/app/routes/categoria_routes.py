from flask import Blueprint
from app.controllers.categoria_controller import CategoriaController
from app.decorators.roles import requiere_rol
from flask_jwt_extended import jwt_required
categoria_bp = Blueprint('categorias', __name__, url_prefix='/categorias')
categoria_bp.route('/', methods=['GET'])(jwt_required()(CategoriaController.listar))
categoria_bp.route('/', methods=['POST'])(requiere_rol('admin')(CategoriaController.crear))
categoria_bp.route('/<int:id>', methods=['PUT'])(requiere_rol('admin')(CategoriaController.editar))
categoria_bp.route('/<int:id>', methods=['DELETE'])(requiere_rol('admin')(CategoriaController.eliminar))