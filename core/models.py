from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Customer(models.Model):

    user = models.OneToOneField(User,null=False,blank=False,on_delete=models.CASCADE)


    phone_field = models.CharField(max_length=12,blank=False)


    def __str__(self):
        return self.user.username


class Car(models.Model):
    name = models.CharField(max_length=100)
    brandname = models.CharField(max_length=100,null='false')
    price = models.FloatField(default=0.0)
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