from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Login_view(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
class Customer(models.Model):
    user = models.ForeignKey(Login_view, on_delete=models.CASCADE, related_name='customer')
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    status1=models.BooleanField(default=0)

class Seller(models.Model):
    user = models.ForeignKey(Login_view, on_delete=models.CASCADE, related_name='seller')
    name = models.CharField(max_length=50)
    pancard_number = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    status2 = models.BooleanField(default=0)


class Manager(models.Model):
    user = models.ForeignKey(Login_view, on_delete=models.CASCADE, related_name='manager')
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=100)
    status3 = models.BooleanField(default=0)

class Mobile_Rentals(models.Model):
    user = models.ForeignKey(Login_view, on_delete=models.CASCADE, related_name='mobile_rentals')
    mobile_name = models.CharField(max_length=50)
    mobile_specification = models.CharField(max_length=150)
    price = models.CharField(max_length=6)
    document = models.FileField(upload_to='documents/')
    status4 = models.BooleanField(default=0)

class Cart(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='add_cart')
    product = models.ForeignKey(Mobile_Rentals, on_delete=models.CASCADE, related_name='add_cart')
    cart_status5 = models.IntegerField(default=0)

class Buy_Now(models.Model):
    user = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='buy_now')
    card_number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    expiry_date =models.CharField(max_length=15)

class Feedback(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='feedback')
    date = models.DateField(auto_now_add=True)
    feedback = models.CharField(max_length=100)
    reply = models.CharField(max_length=150,null=True,blank=True)

class Notification(models.Model):
    date = models.DateField(auto_now_add=True)
    notification = models.CharField(max_length=100)



