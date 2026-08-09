from app.models.producto import Producto

class ProductoFactory:
    @staticmethod
    def crear_producto(name, description, price, category, image_url, is_available=True):
        product = Producto(
            name=name,
            description=description,
            price=price,
            category=category,
            image_url=image_url,
            is_available=is_available
        )
        return product