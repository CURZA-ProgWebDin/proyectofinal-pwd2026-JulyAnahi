from flask import Blueprint, request
from app.controllers.auth_controller import AuthController

auth_bp.route('auth_bp', __name__)

@auth_bp.route('/login',methods=['POST'])

def login():
    data = request.get_json() or {}
    return AuthController.login(data)
