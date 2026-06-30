from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from app.config import Config
from app.database import db

from app.models.base_model import BaseModel
from app.models.rol import Rol
from app.models.user import User
from app.models.categoria import Categoria
from app.models.proveedor import Proveedor
from app.models.producto import Producto
from app.models.movimiento_stock import MovimientoStock

migrate = Migrate()
jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
    
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from app.routes.auth_routes import auth_bp
    from app.routes.categoria_routes import categoria_bp
    from app.routes.proveedor_routes import proveedor_bp
    from app.routes.producto_routes import producto_bp
    from app.routes.movimiento_routes import movimiento_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(categoria_bp)
    app.register_blueprint(proveedor_bp)
    app.register_blueprint(producto_bp)
    app.register_blueprint(movimiento_bp)

    return app