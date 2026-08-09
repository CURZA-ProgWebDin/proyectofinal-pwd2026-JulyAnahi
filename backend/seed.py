from app import create_app
from app.database import db
from app.models.user import User
from app.models.product import Product
from app.factories.user_factory import UserFactory
from app.factories.product_factory import ProductFactory

def seed_database():
    app = create_app()
    with app.app_context():
        print("Initializing database tables...")
        db.create_all()
        
        # 1. Seed Users
        users_to_seed = [
            {"username": "admin", "password": "admin123", "role": "admin"},
            {"username": "cocina", "password": "cocina123", "role": "kitchen"},
            {"username": "caja", "password": "caja123", "role": "cashier"}
        ]
        
        for user_info in users_to_seed:
            existing_user = User.query.filter_by(username=user_info["username"]).first()
            if not existing_user:
                user = UserFactory.create_user(
                    username=user_info["username"],
                    password=user_info["password"],
                    role=user_info["role"]
                )
                db.session.add(user)
                print(f"Seeded user: {user_info['username']} ({user_info['role']})")
            else:
                print(f"User {user_info['username']} already exists.")
                
        # 2. Seed Products (Menu)
        products_to_seed = [
            # Hamburgers
            {
                "name": "Hamburguesa Doble Queso",
                "description": "Doble carne de res premium, queso cheddar fundido, lechuga, tomate y salsa secreta de la casa en pan brioche.",
                "price": 12.50,
                "category": "burgers",
                "image_url": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Hamburguesa de Pollo Crispy",
                "description": "Pechuga de pollo súper crujiente, ensalada de col de la casa, pepinillos y mayonesa picante en pan brioche.",
                "price": 11.00,
                "category": "burgers",
                "image_url": "https://images.unsplash.com/photo-1625813506062-0aeb1d7a094b?auto=format&fit=crop&w=600&q=80"
            },
            
            # Pizzas
            {
                "name": "Pizza Margherita",
                "description": "Salsa de tomate italiana, mozzarella fresca en rodajas, albahaca de nuestro jardín y aceite de oliva virgen extra.",
                "price": 14.00,
                "category": "pizzas",
                "image_url": "https://images.unsplash.com/photo-1604068549290-dea0e4a305ca?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Pizza Pepperoni Special",
                "description": "Salsa marinara, queso mozzarella y una generosa porción de pepperoni premium curado.",
                "price": 16.50,
                "category": "pizzas",
                "image_url": "https://images.unsplash.com/photo-1534308983496-4fabb1a015ee?auto=format&fit=crop&w=600&q=80"
            },
            
            # Drinks
            {
                "name": "Cerveza Artesanal IPA",
                "description": "Cerveza artesanal de la casa, refrescante, con notas cítricas e intensos lúpulos tropicales.",
                "price": 6.00,
                "category": "drinks",
                "image_url": "https://images.unsplash.com/photo-1608270586620-248524c67de9?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Limonada de Menta y Jengibre",
                "description": "Zumo de limón recién exprimido, hojas de menta machacadas y un toque de extracto de jengibre.",
                "price": 4.50,
                "category": "drinks",
                "image_url": "https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?auto=format&fit=crop&w=600&q=80"
            },
            
            # Desserts
            {
                "name": "Volcán de Chocolate",
                "description": "Delicioso bizcocho de chocolate caliente relleno de fudge derretido, acompañado con helado de vainilla premium.",
                "price": 7.50,
                "category": "desserts",
                "image_url": "https://images.unsplash.com/photo-1606313564200-e75d5e30476c?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Cheesecake de Frutos Rojos",
                "description": "Base crujiente de galleta, crema de queso sedosa y coulis dulce de frambuesas y moras silvestres.",
                "price": 8.00,
                "category": "desserts",
                "image_url": "https://images.unsplash.com/photo-1524351199679-46cddf530c04?auto=format&fit=crop&w=600&q=80"
            }
        ]
        
        for prod_info in products_to_seed:
            existing_prod = Product.query.filter_by(name=prod_info["name"]).first()
            if not existing_prod:
                product = ProductFactory.create_product(
                    name=prod_info["name"],
                    description=prod_info["description"],
                    price=prod_info["price"],
                    category=prod_info["category"],
                    image_url=prod_info["image_url"]
                )
                db.session.add(product)
                print(f"Seeded product: {prod_info['name']}")
            else:
                print(f"Product {prod_info['name']} already exists.")
                
        db.session.commit()
        print("Database seeding completed successfully!")

if __name__ == "__main__":
    seed_database()
