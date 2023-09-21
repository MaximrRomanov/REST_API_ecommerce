from django.contrib import admin
from django.urls import path
from .views import ProductListAPIView, ProductDetailAPIView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("api/products/", ProductListAPIView.as_view(), name="products_list"),
    path(
        "api/products/<int:pk>/", ProductDetailAPIView.as_view(), name="product_detail"
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
