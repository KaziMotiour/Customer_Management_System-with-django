from django.urls import path
from .views import home, customer, product, update_order, delete_order
app_name='accounts'
urlpatterns = [
    path('',home, name='home'),
    path('customer/<str:pk>/', customer, name='customer'),
    path('product/', product, name='product'),
    path('update_order/<str:pk>/', update_order, name='UpdateOrder'),
    path('delete_order/<str:pk>/', delete_order, name='DeleteOrder'),
]