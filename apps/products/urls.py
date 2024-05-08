from django.urls import path
from apps.products.views import ProductViewSet, ProductDetailAPI


urlpatterns = [
    path('api/products/', ProductViewSet.as_view(), name='api_products'),
    path('api/products/<int:pk>/', ProductDetailAPI.as_view(), name="api_product_detail")
]