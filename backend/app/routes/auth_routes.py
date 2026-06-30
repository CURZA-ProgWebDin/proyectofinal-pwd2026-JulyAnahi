from flask import Blueprint
from app.controllers.auth_controller import AuthController
from app.decorators.roles import requiere_rol
from flask_jwt_extended import jwt_required

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
auth_bp.strict_slashes = False

auth_bp.route('/register', methods=['POST'])(AuthController.register)
auth_bp.route('/login', methods=['POST'])(AuthController.login)
auth_bp.route('/me', methods=['GET'])(jwt_required()(AuthController.me))

auth_bp.route('/users', methods=['GET'])(requiere_rol('admin')(AuthController.listar_usuarios))
auth_bp.route('/users/<int:id>', methods=['PUT'])(requiere_rol('admin')(AuthController.editar_usuario))
auth_bp.route('/users/<int:id>', methods=['DELETE'])(requiere_rol('admin')(AuthController.eliminar_usuario))
