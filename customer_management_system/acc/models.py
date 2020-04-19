from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    phone=models.CharField(max_length=250)
    profile_pic=models.ImageField(upload_to='profile_pic', null=True, blank=True)
    create_date=models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return str(self.name)

class Product(models.Model):
    CATAGORY=(
        ('indoor','indoor'),
        ('Out Door', 'Out Door')
    )
    name=models.CharField(max_length=250)
    price=models.CharField(max_length=250, null=True,blank=True)
    category=models.CharField(max_length=250, null=True, blank=True, choices=CATAGORY)
    description=models.CharField(max_length=500, null=True, blank=True)
    product_pic=models.ImageField(upload_to='profile_pic', null=True, blank=True)
    create_date=models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return str(self.name)

class Order(models.Model):
    STATUS=(
        ('pending','pending'),
        ('Out of delivery','Out of delivery'),
        ('Delivered','Delivered')
    )
    date_created=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status=models.CharField(max_length=250, null=True, choices=STATUS)
    