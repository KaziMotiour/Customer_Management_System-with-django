from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import Customer, Product, Order
from .forms import OrderForm, CustomerForm

def home(request):
    last_5_order = Order.objects.filter().order_by('-date_created')[:5]
    total_order= Order.objects.all()
    customer = Customer.objects.all()
    order_deliverd=Order.objects.filter(status='Delivered').count()
    order_pending=Order.objects.filter(status='pending').count()
    
    form=OrderForm() # order create form
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    cusotmerForm=CustomerForm() # Cusotmer creat form
    if request.method == 'POST':
        cusotmerForm = CustomerForm(request.POST)
        if cusotmerForm.is_valid():
            cusotmerForm.save()
            return redirect('/')


    context={
        'order':total_order,
        'customer':customer,
        'deliverd_order':order_deliverd,
        'pending_order':order_pending,
        'last_5_orders':last_5_order,
        'form':form,
        'cusotmerForm':cusotmerForm
        
    }

    return render(request, 'accounts/Dashboard.html',context) 


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


def update_order(request,pk):
    orders=Order.objects.get(id=pk)
    form = OrderForm(instance=orders)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=orders)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}
    return render(request,'accounts/Update_order.html',context)

def delete_order(request, pk):
    orders = Order.objects.get(pk=pk)
    if request.method=="POST":
        orders.delete()
        return redirect('/')
    context={'item':orders}
    return render(request, 'accounts/Delete_order.html', context)