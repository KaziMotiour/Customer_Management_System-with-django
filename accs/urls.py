from django.urls import path
from .views import(
     home, customer, product, update_order, delete_order, 
     update_customer, delete_customer, registration,login, logout)
app_name='accounts'
urlpatterns = [
    path('',home, name='home'),
    path('registration',registration, name='registration'),
    path('login',login, name='login'),
    path('logout',logout, name='logout'),
    path('customer/<str:pk>/', customer, name='customer'),
    path('customer/<str:pk>/update', update_customer, name='CustomerUpdate'),
    path('customer/<str:pk>/delete', delete_customer, name='CustomerDelete'),
    path('product/', product, name='product'),
    path('update_order/<str:pk>/', update_order, name='UpdateOrder'),
    path('delete_order/<str:pk>/', delete_order, name='DeleteOrder'),
]