from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'accounts/Dashboard.html') 

def customer(request):
    return render(request,'accounts/Customer.html')

def product(request):
    return render(request, 'accounts/Product.html')