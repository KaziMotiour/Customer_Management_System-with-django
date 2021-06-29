from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.http import HttpResponse
from .models import Customer, Product, Order
from .forms import OrderForm, CustomerForm, UserRegistrationForm, AddProduct
from django.forms import inlineformset_factory
from .filter import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .decorator import unauthorize_user, allow_user
from django.contrib.auth.models import Group
from django.contrib.auth.models import User


@unauthorize_user
def registration(request):

  if request.method == "POST" :
      form = UserRegistrationForm(request.POST, request.FILES) #since request.POST is present, populate the form with POST values
      if form.is_valid(): #Check if its valid
          # print ("form is valid")
          user = form.save()
          group = Group.objects.get(name='customer')
          user.groups.add(group)
          username=form.cleaned_data.get('username')
          
          messages.success(request, 'Registration Complete for '+username)
          return redirect("/login")
      else: #invalid case
          print (form.is_valid())   #form contains data and errors
          print (form.errors)
  else:
      form = UserRegistrationForm() #No post dat
  context={'form':form}
  return render(request, 'accounts/registration.html',context)
    

@unauthorize_user
def login(request):

    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password incorrect')
    context={}
    return render(request, 'accounts/login.html',context)


def logout(request):
    auth_logout(request)
    return redirect('/login')




@login_required(login_url='/product')
@allow_user(allowed_user=['admin'])
def home(request):
    last_5_order = Order.objects.filter(status='pending').order_by('-date_created')[:5]
    total_order= Order.objects.all()
    customer = User.objects.all()
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



@login_required(login_url='accounts:login')
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


@login_required(login_url='accounts:login')
def delete_order(request, pk):
    orders = Order.objects.get(pk=pk)
    if request.method=="POST":
        orders.delete()
        return redirect('/')
    context={'item':orders}
    return render(request, 'accounts/Delete_order.html', context)




@login_required(login_url='accounts:login')
def customer(request,pk):

    OrderFormSet=inlineformset_factory(Customer, Order, fields=('product',),extra=5)

    queryset=User.objects.get(pk=pk)
    order = queryset.customer.customer.all()


    form=OrderForm(initial={'coustomer':queryset.customer}) # order create form
    formset=OrderFormSet(queryset=Order.objects.none(), instance=queryset.customer)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=queryset.customer)
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


@login_required(login_url='accounts:login')
def update_customer(request,pk):
    customer=User.objects.get(pk=pk)
    customer_form=CustomerForm(instance=customer.customer)
    if request.method=="POST":
        customer_form=CustomerForm(request.POST, request.FILES, instance=customer.customer)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('/customer/'+pk)

    context={
        'customer_form':customer_form
        }
    
    return render(request,'accounts/Customer_Update.html',context)


@login_required(login_url='accounts:login')
def delete_customer(request, pk):
    customer = Customer.objects.get(pk=pk)
    if request.method=="POST":
        customer.delete()
        return redirect("/")
    context={'customer':customer}
    return render(request,'accounts/Customer_Delete.html',context)



def product(request):

    queryset=Product.objects.all()
    form=AddProduct()
    if request.method=="POST":
        form=AddProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/product')

    context={
        'queryset':queryset,
        'form':form,
    }

    return render(request, 'accounts/Product.html',context)

