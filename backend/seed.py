from app import create_app
from app.database import db
from app.models.rol import Rol
from app.models.user import User
from app.models.categoria import Categoria
from app.models.proveedor import Proveedor
from app.models.producto import Producto

app = create_app()

with app.app_context():
    # Asegura la creación de las tablas bajo el contexto activo
    db.create_all()

    if not Rol.query.filter_by(nombre='admin').first():
        rol_admin = Rol(nombre='admin')
        rol_op = Rol(nombre='operador')
        db.session.add_all([rol_admin, rol_op])
        db.session.commit()
        
        # Creación de usuarios con sus contraseñas encriptadas de forma segura
        admin = User(username='admin', email='admin@stock.com', rol_id=rol_admin.id)
        admin.generate_password('admin123')

        operador = User(username='operador', email='operador@stock.com', rol_id=rol_op.id)
        operador.generate_password('operador123')

        db.session.add_all([admin, operador])

        cat = Categoria(nombre='Almacen', descripcion='Bienes secos')
        prov = Proveedor(nombre='Distribuidora Norte', contacto='Carlos Albornoz', telefono='1234567', email='proveedo@norte.com')
        db.session.add_all([cat, prov])
        db.session.commit()

        prod = Producto(nombre='fideos 500g', descripcion='fideos secos', precio_costo=10.00, precio_venta=15.00, stock_actual=20, stock_minimo=5, categoria_id=cat.id, proveedor_id=prov.id)
        db.session.add(prod)
        db.session.commit()
        
        print('===================================================')
        print('   POBLADO INICIAL PARA DESARROLLO EXITOSO')
        print('===================================================')