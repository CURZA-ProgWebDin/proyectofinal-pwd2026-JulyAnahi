from flask import Blueprint
from app.controllers.movimiento_controller import MovimientoController
from app.decorators.roles import requiere_rol
from flask_jwt_extended import jwt_required
movimiento_bp = Blueprint('movimientos', __name__, url_prefix='/movimientos')
movimiento_bp.route('/', methods=['GET'])(requiere_rol('admin')(MovimientoController.listar_todos))
movimiento_bp.route('/mis/', methods=['GET'])(jwt_required()(MovimientoController.listar_mis))
movimiento_bp.route('/', methods=['POST'])(jwt_required()(MovimientoController.registrar))