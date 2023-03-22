from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):

    user = models.OneToOneField(User,null=False,blank=False,on_delete=models.CASCADE)
    firstname = models.CharField(default=False, max_length=100)
    lastname = models.CharField(default=False, max_length=100)
    email = models.EmailField(default=False, max_length=50)
    phone_field = models.CharField(max_length=12,blank=False)


    def __str__(self):
        return self.user.username
class Dealer(models.Model):

    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)
    firstname = models.CharField(default=False, max_length=100)
    lastname = models.CharField(default=False, max_length=100)
    email = models.EmailField(default=False, max_length=50)
    phone_field = models.CharField(max_length=12,blank=False)


    def __str__(self):
        return self.user.username

class Car(models.Model):
    name = models.CharField(max_length=100)
    brandname = models.CharField(max_length=100,null='false')
    price_per_day = models.FloatField(default=0.0)
    price_per_hr = models.FloatField(default=0.0)
    price_per_week = models.FloatField(default=0.0)
    fuel_price = models.FloatField(default=0.0)
    seats = models.IntegerField(default=0)
    mileage = models.IntegerField(default=0)
    luggage= models.IntegerField(default=0)
    transmission = models.CharField(default=False,max_length=100)
    fuel_type = models.CharField(default=False,max_length=100)


    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Contact_us(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email