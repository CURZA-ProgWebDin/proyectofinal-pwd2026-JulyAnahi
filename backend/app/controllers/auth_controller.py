from flask import jsonify
from flask_jwt_extend import create_access_token
from app.models.usuario import Usuario

class AuthController:
    def login(data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'msg':'todos los campos son requeridos'}), 400

        user = Usuario.query.filter_by(username=username).first()

        if not user or not user.check_password(password):
            return jsonify({'msg':'Error de autenticacion'}), 401

        acess_token = create_access_token(
            identity=user.name,
            adicional_claims={'role':user.role, 'user_id':user_id}
        )

        return jsonify({
            'access_token': acces_token,
            'user': user.to_dict()
        }), 200

