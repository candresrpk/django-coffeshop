
from django.urls import path
from .views import ProductFormView, ProductsListView

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='list_products'),
    path('add/', ProductFormView.as_view(), name='add_product'),
]
