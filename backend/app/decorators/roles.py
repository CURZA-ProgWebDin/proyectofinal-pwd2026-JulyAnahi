from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_inrequest, get_jwt

def requiere_rol(*roles):
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            try:
                verify_jwt_in_request()
            except Exception as e:
                return jsonify({'msg':'Autorizacion invalida', 'error':str(e)}), 401

            claims = get_jwt()
            user_role = claims.get('role')

            if user_role == 'admin':
                return func(*args, **kwargs)
            
            if user_role not in roles:
                return jsonify({"msg": "Acceso prohibido rol insuficiente"})

            return func(*args, **kwargs)
        return decorated_function
    return decorator