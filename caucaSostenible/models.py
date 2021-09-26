from django.db import models
from django.contrib.auth.models import AbstractUser

class Event(models.Model):
   name = models.CharField(max_length=60)
   description = models.CharField(max_length=600)

class Investor(models.Model):
   name = models.CharField(max_length=60)
   description = models.CharField(max_length=600)
   email = models.CharField(max_length=100)
   imgURL = models.CharField(max_length=300)

class User(AbstractUser):
   pass

class Bill(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   total = models.FloatField()

class Product(models.Model):
   name = models.CharField(max_length=60)
   price = models.FloatField()
   discount = models.FloatField()
   description = models.CharField(max_length=300)
   imgURL = models.CharField(max_length=300)

class BillDetail(models.Model):
   bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   
   class Meta: # Composite pk
        unique_together = (('bill', 'product'),)

class Undertaking(models.Model):
   name = models.CharField(max_length=60)
   description = models.CharField(max_length=600)
   location = models.CharField(max_length=40)
   phone = models.IntegerField()
   imgURL = models.CharField(max_length=300)