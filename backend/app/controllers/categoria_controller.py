from flask import request, jsonify
from app.database import db
from app.models.categoria import Categoria

class CategoriaController:
    @staticmethod
    def listar():
        return jsonify([{"id": c.id, "nombre": c.nombre, "descripcion": c.descripcion} for c in Categoria.query.all()]), 200

    @staticmethod
    def crear():
        data = request.get_json() or {}
        nuevo = Categoria(nombre=data['nombre'], descripcion=data.get('descripcion'))
        db.session.add(nuevo)
        db.session.commit()
        return jsonify({"msg": "Creada"}), 201

    @staticmethod
    def editar(id):
        c = Categoria.query.get_or_404(id)
        data = request.get_json() or {}
        c.nombre = data.get('nombre', c.nombre)
        c.descripcion = data.get('descripcion', c.descripcion)
        db.session.commit()
        return jsonify({"msg": "Actualizada"}), 200

    @staticmethod
    def eliminar(id):
        c = Categoria.query.get_or_404(id)
        if len(c.productos) > 0:
            return jsonify({"msg": "Conflict: Asociado a productos"}), 409
        db.session.delete(c)
        db.session.commit()
        return jsonify({"msg": "Eliminada"}), 200