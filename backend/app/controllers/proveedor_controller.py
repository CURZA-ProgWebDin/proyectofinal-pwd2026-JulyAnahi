from flask import request, jsonify
from app.database import db
from app.models.proveedor import Proveedor

class ProveedorController:
    @staticmethod
    def listar():
        return jsonify([{"id": p.id, "nombre": p.nombre, "contacto": p.contacto, "telefono": p.telefono, "email": p.email} for p in Proveedor.query.all()]), 200

    @staticmethod
    def crear():
        data = request.get_json() or {}
        nuevo = Proveedor(nombre=data['nombre'], contacto=data.get('contacto'), telefono=data.get('telefono'), email=data.get('email'))
        db.session.add(nuevo)
        db.session.commit()
        return jsonify({"msg": "Creado"}), 201

    @staticmethod
    def editar(id):
        p = Proveedor.query.get_or_404(id)
        data = request.get_json() or {}
        p.nombre = data.get('nombre', p.nombre)
        p.contacto = data.get('contacto', p.contacto)
        p.telefono = data.get('telefono', p.telefono)
        p.email = data.get('email', p.email)
        db.session.commit()
        return jsonify({"msg": "Actualizado"}), 200

    @staticmethod
    def eliminar(id):
        p = Proveedor.query.get_or_404(id)
        if len(p.productos) > 0:
            return jsonify({"msg": "Conflict: Asociado a productos"}), 409
        db.session.delete(p)
        db.session.commit()
        return jsonify({"msg": "Eliminado"}), 200