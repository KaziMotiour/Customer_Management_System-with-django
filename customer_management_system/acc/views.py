from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.http import HttpResponse
from .models import Customer, Product, Order
from .forms import OrderForm, CustomerForm
from django.forms import inlineformset_factory
from .filter import OrderFilter

def home(request):
    last_5_order = Order.objects.filter().order_by('-date_created')[:5]
    total_order= Order.objects.all()
    customer = Customer.objects.all()
    order_deliverd=Order.objects.filter(status='Delivered').count()
    order_pending=Order.objects.filter(status='pending').count()
    
    
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
        'cusotmerForm':cusotmerForm
        
    }

    return render(request, 'accounts/Dashboard.html',context) 



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




def customer(request,pk):

    OrderFormSet=inlineformset_factory(Customer, Order, fields=('product','status'),extra=5)

    queryset=Customer.objects.get(pk=pk)
    order = queryset.customer.all()

    # form=OrderForm(initial={'coustomer':queryset}) # order create form
    formset=OrderFormSet(queryset=Order.objects.none(), instance=queryset)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=queryset)
        if formset.is_valid():
            formset.save()
            return redirect('/customer/'+pk)

    serach_order = OrderFilter(request.GET, queryset=order)
    order = serach_order.qs

    context={
        'customer':queryset,
        'order':order,
        'formset':formset,
        'serach_order':serach_order

    }
    return render(request,'accounts/Customer.html',context)


def update_customer(request,pk):
    customer=Customer.objects.get(pk=pk)
    customer_form=CustomerForm(instance=customer)
    if request.method=="POST":
        customer_form=CustomerForm(request.POST, instance=customer)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('/customer/'+pk)

    context={
        'customer_form':customer_form
        }
    
    return render(request,'accounts/Customer_Update.html',context)

def delete_customer(request, pk):
    customer = Customer.objects.get(pk=pk)
    if request.method=="POST":
        customer.delete()
        return redirect("/")
    context={'customer':customer}
    return render(request,'accounts/Customer_Delete.html',context)



def product(request):

    queryset=Product.objects.all()
    return render(request, 'accounts/Product.html',{'context':queryset})

