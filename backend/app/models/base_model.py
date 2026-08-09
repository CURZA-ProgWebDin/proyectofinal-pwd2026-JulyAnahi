from datetime import datetime
from app.database import db

class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow )

    #agrego la funcion que convierte el modelo al diccionario aca para no tener que hacerlo en cada modelo
    def to_dict(self):
        #para no exponer el  campo de la password
        hidden_fields = getattr(self, '_hidden_fields', [])
        data = {} 

        for column in self.__table__.columns:
            if column.name in hidden_fields:
                continue

            value = getattr(self, column.name)

            if isinstance(value, datetime):
                data[column.name] = value.isoformat()
            else:
                data[column.name] = value
        return data





