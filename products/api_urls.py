from django.urls import path
from .api_views import ProductListCreateView, ProductDetailView

urlpatterns = [
    path('api/products/', ProductListCreateView.as_view(),
         name='api-product-list-create'),
    path('api/products/<int:pk>/', ProductDetailView.as_view(),
         name='api-product-detail'),
]
