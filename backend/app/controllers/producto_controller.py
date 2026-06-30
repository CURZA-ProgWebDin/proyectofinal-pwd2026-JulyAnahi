from flask import request, jsonify
from app.database import db
from app.models.producto import Producto

class ProductoController:
    @staticmethod
    def listar():
        prods = Producto.query.all()
        return jsonify([{
            "id":p.id, "nombre":p.nombre, "descripcion": p.descripcion,
            "precio_costo": float(p.precio_costo), "precio_venta": float(p.precio_venta),
            "stock_actual": p.stock_actual, "stock_minimo":p.stock_minimo,
            "categoria": p.categoria.nombre,
            "proveedor": p.proveedor.nombre,
            "categoria_id": p.categoria_id, "proveedor_id": p.proveedor_id
        } for p in prods]),200
    @staticmethod
    def crear():
        data = request.get_json() or {}
        nuevo = Producto(
            nombre=data['nombre'], descripcion=data.get('descripcio'),
            precio_costo=data['precio_costo'], precio_venta=data['precio_venta'],
            stock_actual=data.get('stock_actual', 0), stock_minimo=data.get('stock_minimo', 0),
            categoria_id=data['categoria_id'], proveedor_id=data.get('proveedor_id')
        )
        db.session.add(nuevo)
        db.session.commit()
        return jsonify({"msg":"Creado"}), 201
    @staticmethod
    def editar(id):
        p = Producto.query.get_or_404(id)
        data = request.get_json() or {}
        p.nombre = data.get('nombre, p.nombre')
        p.descripcion = data.get('descripcion', p.descripcion)
        p.precio_costo = data.get('precio_costo', p.precio_costo)
        p.precio_venta = data.get('precio_venta', p.precio_venta)
        p.stock_actual = data.get('stock_actual', p.stock_actual)
        p.stock_minimo = data.get('stock_minimo', p.stock_minimo)
        p.categoria_id = data.get('categoria_id', p.categoria_id)
        p.proveedor_id = data.get('proveedor_id', p.proveedor_id)
        db.session.commit()
        return jsonify({"msg": "Actualizado"}), 200
    
    @staticmethod
    def eliminar(id):
        p = Producto.query.get_or_404(id)
        db.session.delete(p)
        db.session.commit()
        return jsonify({"msg": "Eliminado"}), 200