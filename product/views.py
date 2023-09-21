from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Product
from .serializer import ProductSerializer


class ProductListAPIView(ListCreateAPIView):
    """
    Может вывести список товаров при get-запросе,
    может создать новый продукт при post-запросе

    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Может обновить продукт в БД при put-запросе (update)
    Может получить экземпляр объекта из БД при get-запросе (retrieve)
    Может удалить продукт из БД при delete-запросе (destroy)

    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
