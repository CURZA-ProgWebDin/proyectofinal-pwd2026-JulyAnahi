from flask import Blueprint
from app.controllers.auth_controller import AuthController
from app.utils.roles import requiere_rol

auth_bp = Blueprint('auth', __name__)

auth_bp.route('/register', methods=['POST'])(AuthController.register)
auth_bp.route('/login', methods=['POST'])(AuthController.login)

auth_bp.route('/me', methods=['GET'])(requiere_rol('admin', 'administrador', 'operador')(AuthController.me))
auth_bp.route('/usuarios', methods=['GET'])(requiere_rol('admin', 'administrador')(AuthController.listar_usuarios))
auth_bp.route('/usuarios/<int:id>', methods=['PUT'])(requiere_rol('admin', 'administrador')(AuthController.editar_usuario))
auth_bp.route('/usuarios/<int:id>', methods=['DELETE'])(requiere_rol('admin', 'administrador')(AuthController.eliminar_usuario))