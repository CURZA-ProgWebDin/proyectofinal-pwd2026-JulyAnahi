from flask import request, jsonify
from app.database import db
from app.models.movimiento_stock import MovimientoStock
from app.models.producto import Producto
from flask_jwt_extended import get_jwt_identity

class MovimientoController:
    @staticmethod
    def listar_todos():
        movs = MovimientoStock.query.all()
        return jsonify([{
            "id": m.id, "tipo": m.tipo, "cantidad": m.cantidad, "motivo": m.motivo,
            "producto": m.producto_relacion.nombre, "user_id": m.user_id, "created_at": m.created_at
        } for m in movs]), 200

    @staticmethod
    def listar_mis():
        user_id = get_jwt_identity()
        movs = MovimientoStock.query.filter_by(user_id=int(user_id)).all()
        return jsonify([{
            "id": m.id, "tipo": m.tipo, "cantidad": m.cantidad, "motivo": m.motivo,
            "producto": m.producto_relacion.nombre, "created_at": m.created_at
        } for m in movs]), 200

    @staticmethod
    def registrar():
        user_id = get_jwt_identity()
        data = request.get_json() or {}
        tipo = data.get('tipo')
        cantidad = data.get('cantidad')
        producto_id = data.get('producto_id')

        if tipo not in ['entrada', 'salida']: return jsonify({"msg": "Tipo inválido"}), 400
        if not cantidad or cantidad <= 0: return jsonify({"msg": "Cantidad inválida"}), 400

        producto = Producto.query.get(producto_id)
        if not producto: return jsonify({"msg": "Producto inexistente"}), 404

        if tipo == 'entrada':
            producto.stock_actual += cantidad
        elif tipo == 'salida':
            if producto.stock_actual - cantidad < 0:
                return jsonify({"msg": f"Stock insuficiente. Disponible: {producto.stock_actual}"}), 400
            producto.stock_actual -= cantidad

        nuevo = MovimientoStock(tipo=tipo, cantidad=cantidad, motivo=data.get('motivo'), producto_id=producto_id, user_id=int(user_id))
        db.session.add(nuevo)
        db.session.commit()
        return jsonify({"msg": "Movimiento guardado exitosamente"}), 201