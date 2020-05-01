from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save

# Create your models here.




class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, blank=True)
    name=models.CharField(max_length=250, null=True, blank=True)
    email=models.CharField(max_length=250 ,null=True, blank=True)
    phone=models.CharField(max_length=250, null=True, blank=True)
    profile_pic=models.ImageField(upload_to='profile_pic', null=True, blank=True)
 
    create_date=models.DateTimeField(auto_now_add=True, null=True,  blank=True)


    def __str__(self):
        return str(self.user)

def customer_save_user_instance(sender,instance,created, *args, **kwargs):
    print(instance)
    if created:
        new_profile=Customer.objects.get_or_create(user=instance)

post_save.connect(customer_save_user_instance, sender=settings.AUTH_USER_MODEL)

class Tag(models.Model):
    tag_name=models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.tag_name)

class Product(models.Model):
    CATAGORY=(
        ('Indoor','Indoor'),
        ('Out Door', 'Out Door')
    )
    name=models.CharField(max_length=250)
    price=models.CharField(max_length=250, null=True,blank=True)
    category=models.CharField(max_length=250, null=True, blank=True, choices=CATAGORY)
    description=models.CharField(max_length=500, null=True, blank=True)
    product_pic=models.ImageField(upload_to='profile_pic', null=True, blank=True)
    tag_name=models.ManyToManyField(Tag)
    create_date=models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return str(self.name)

class Order(models.Model):
    STATUS=(
        ('pending','pending'),
        ('Out of delivery','Out of delivery'),
        ('Delivered','Delivered')
    )
    coustomer=models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    date_created=models.DateTimeField(auto_now_add=True,)
    status=models.CharField(max_length=250, null=True, choices=STATUS)

    def __str__(self):
        return str(self.product.name)
    

class Users(models.Model):
    name=models.CharField(max_length=200, null=True)