from django.contrib import admin
from .models import Customer, Product, Order, Tag
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)


# Register your models here.
