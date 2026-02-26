from django.urls import path
from .view.product_view import ProductListCreateView, product_detail

urlpatterns = [
    # Para POST y GET (todos)
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    
    # PARA UPDATE Y DELETE (necesita el <int:pk>)
    path('products/<int:pk>/', product_detail, name='product-detail'),
]