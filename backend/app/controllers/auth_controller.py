from flask import request, jsonify
from app.database import db
from app.models.user import User
from app.models.rol import Rol
from flask_jwt_extended import create_access_token, get_jwt_identity

class AuthController:
    @staticmethod
    def register():
        data = request.get_json() or {}
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        rol_nombre = data.get('rol', 'operador')

        if '(' in rol_nombre:
            rol_nombre = rol_nombre.split('(')[-1].replace(')', '').strip()

        if not username or not email or not password:
            return jsonify({"msg": "Campos incompletos"}), 400

        if User.query.filter((User.username == username) | (User.email == email)).first():
            return jsonify({"msg": "Usuario o Email ya existente"}), 400
        
        rol_obj = Rol.query.filter_by(nombre=rol_nombre).first()
        if not rol_obj:
            return jsonify({"msg": f"Rol '{rol_nombre}' no válido"}), 400
            
        nuevo = User(username=username, email=email, rol_id=rol_obj.id)
        nuevo.generate_password(password)
        db.session.add(nuevo)
        db.session.commit()
        return jsonify({"msg": "Usuario registrado"}), 201

    @staticmethod
    def login():
        data = request.get_json() or {}
        user = User.query.filter_by(username=data.get('username')).first()
        if user and user.check_password(data.get('password')):
            token = create_access_token(identity=str(user.id), additional_claims={"rol": user.rol_relacion.nombre})
            return jsonify(access_token=token), 200
        return jsonify({"msg": "Credenciales inválidas"}), 401

    @staticmethod
    def me():
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        if not user:
            return jsonify({"msg": "No encontrado"}), 404
        return jsonify({"id": user.id, "username": user.username, "email": user.email, "rol": user.rol_relacion.nombre}), 200

    @staticmethod
    def listar_usuarios():
        usuarios = User.query.all()
        return jsonify([{"id": u.id, "username": u.username, "email": u.email, "rol": u.rol_relacion.nombre} for u in usuarios]), 200

    @staticmethod
    def editar_usuario(id):
        user = User.query.get(id)
        if not user:
            return jsonify({"msg": "Usuario no encontrado"}), 404
        data = request.get_json() or {}
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        
        if data.get('rol'):
            rol_obj = Rol.query.filter_by(nombre=data.get('rol')).first()
            if rol_obj:
                user.rol_id = rol_obj.id

        if data.get('password'):
            user.generate_password(data.get('password'))

        db.session.commit()
        return jsonify({"msg": "Usuario actualizado"}), 200

    @staticmethod
    def eliminar_usuario(id):
        user = User.query.get(id)
        if not user:
            return jsonify({"msg": "Usuario no encontrado"}), 404
        if len(user.movimientos) > 0:
            return jsonify({"msg": "Conflict: El usuario registra movimientos de stock asociados"}), 409
        db.session.delete(user)
        db.session.commit()
        return jsonify({"msg": "Usuario eliminado"}), 200