from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
from app.database import db, migrate

jwt = JWTManager()

def create_app(config_class=Config):
    app =Flask(__name__)
    app.config.from_object(config_class)

    CORS(app, resources={r'/api/*':{'origins':'*'}})
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from app.routes.auth_routes import auth_bp
    from app.routes.admin_routes import admin_bp
    from app.routes.orden_routes import order_bp
    from app.routes.producto_routes import product_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    app.register_blueprint(order_bp, url_prefix='/api/orders')
    app.register_blueprint(product_bp, url_prefix='/api/products')
    return app