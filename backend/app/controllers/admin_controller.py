from flask import jsonify
from app.database import db
from app.models.usuario import Usuario
from app.models.producto import Producto
from app.factories.usuario_factory import UsuarioFactory
from app.factories.producto_factory import ProductoFactory


class AdminController:

    @staticmethod
    def get_users():
        users = Usuario.query.all()
        return jsonify([user.to_dict() for user in users]), 200

    @staticmethod
    def create_user(data):
        username = data.get('username')
        password = data.get('password')
        role = data.get('role')
        if not username or not password or not role:
            return jsonify({'mensaje':'Faltan campos obligatorios'}), 400

        if role not in ['admin', 'cocina','caja']:
            return jsonify({'mensaje':'rol invalido'}), 400

        if Usuario.query.filter_by(username=username).first():
            return jsonify({'mensaje':'Error al crear el usuario intenta con otro nombre'}), 400

        user = UsuarioFactory.crear_usuario(username, password, role)
        db.session.add(user)
        db.seeion.commit()
        return jsonify(user.to_dict()), 201 

    @staticmethod
    def update_user(user_id, data):
        user = Usuario.query.get(user_id)
        if not user:
            return jsonify({'mensaje': 'Usuario no encontrado'}), 404

        username = data.get('username')
        password = data.get('password')
        role = data.get('role')


        if username:
            existe = Usuario.query.filter_by(username=username).first()
            if existe and existe.id != user_id:
                return jsonify({'mensaje':'Error de actualizacion de usuario'}), 409
            user.username=username

        if role:
            if role not in ['admin', 'cocina', 'caja']:
                return jsonify({'msg':'Rol invalido'}), 400
            user.role = role
        if password:
            user.set_password(password)

        db.session.commit()
        return jsonify(user.to_dict()), 200

    @staticmethod
    def delete_user(user_id):
        user = Usuario.query.get(user_id)
        if not user:
            return jsonify({'msg':'Usuario no encontrado'}), 404

    #PRODUCTOS LO PONGO ACA POR QUE SOLO EL ADMINISTRADOR PUEDE ACCEDER AL CRUD DE PRODUCTOS
    @staticmethod
    def get_products():
        products = Producto.query.all()
        return jsonify([product.to_dict() for product in products]), 200


    @staticmethod
    def create_product(data):
       name = data.get('name')
       price = data.get('price')
       category = data.get('category')
       description = data.get('description','')
       image_url = data.get('image_url', '')
       is_available = data.get('is_avaiable')

       if not name or price is None or not category:
           return jsonify({'msg':'El nombre la categoria y el precio son campos obligatorios'})

       try:
           price = float(price)
       except ValueError:
           description = db.Column(db.Text, nullable=True)
           return jsonify({'msg':'El precio debe ser un numerico'}), 400

       product = ProductoFactory.create_product(name, description, price, category, image_url, is_available)
       db.session.add(product)
       db.session.commit()
       return jsonify(product.to_dict()), 201
       

    @staticmethod
    def update_product(product_id, data):
        product =  Producto.query.get(product_id)
        if not product:
            return jsonify({'menssage':'El producto no existe'}), 404             
        if 'name' in data:
            product.name = data['name']
        if 'price' in data:
            try:
                product.price= float(data['price'])
            except ValueError:
                return jsonify({'msg':'El precio debe ser numerico'}), 400
        if 'category' in data:
            product.category = data['category']
        if 'description' in data:
            product.description = data['description']
        if 'image_url' in data:
            product.image_url = data['image_url']
        if 'is_available'in data:
            product.is_available = bool(data['is_available'])

        db.session.commit()
        return jsonify(product.to_dict()), 200

    @staticmethod
    def delete_product(product_id):
        product = Producto.query.get(product_id)
        if not product:
            return jsonify({'msg':'El producto no existe'}), 404

        db.session.delete(product)
        db.session.commit()
        return jsonify({'msg':'Producto eliminado exitosamente'}), 200
   
       
