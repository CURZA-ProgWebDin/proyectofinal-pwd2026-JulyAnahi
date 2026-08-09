from flask import Blueprint
from app.controllers.admin_controller import AdminController

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('', methods=['GET'])
@product_bp.route('/', methods=['GET'])
def get_products():
    return AdminController.get_products()
