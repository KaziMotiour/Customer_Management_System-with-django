from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Order, Customer, Product


class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields='__all__'

class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields=['user','name','email','phone','profile_pic']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class AddProduct(ModelForm):
    class Meta:
        model=Product
        fields='__all__'