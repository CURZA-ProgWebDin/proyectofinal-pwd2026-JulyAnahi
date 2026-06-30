from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt

def requiere_rol(*roles_permitidos):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            user_role = claims.get('rol')
            if user_role not in roles_permitidos:
                return jsonify({"msg": "Acceso prohibido: Rol insuficiente"}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator