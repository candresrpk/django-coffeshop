from django.urls import path
from .views import MyOrderView, CreateOrderProductView

app_name = 'orders'


urlpatterns = [
    path('',MyOrderView.as_view(), name='my_orders' ),
    path('add-item/', CreateOrderProductView.as_view(), name='add-item' ),
    
]
