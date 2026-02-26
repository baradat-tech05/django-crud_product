from ..model.models import Product
class ProductService:
    
    @staticmethod
    def create_product(**data) -> Product:
        return Product.objects.create(**data)
    
    @staticmethod
    def list_products():
        return Product.objects.all().order_by("-id")