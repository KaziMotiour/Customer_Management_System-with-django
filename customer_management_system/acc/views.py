from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Product, Order

def home(request):
    last_5_order = Order.objects.all()[0:5]
    total_order= Order.objects.all()
    customer = Customer.objects.all()
    order_deliverd=Order.objects.filter(status='Delivered').count()
    order_pending=Order.objects.filter(status='pending').count()

    context={
        'order':total_order,
        'customer':customer,
        'deliverd_order':order_deliverd,
        'pending_order':order_pending,
        'last_5_orders':last_5_order,
        
    }

    return render(request, 'accounts/Dashboard.html',{'context':context}) 

def customer(request,pk):
    queryset=Customer.objects.get(pk=pk)
    order = queryset.customer.all()
    context={
        'customer':queryset,
        'order':order,

    }
    return render(request,'accounts/Customer.html',{'context':context})

def product(request):
    queryset=Product.objects.all()
    return render(request, 'accounts/Product.html',{'context':queryset})