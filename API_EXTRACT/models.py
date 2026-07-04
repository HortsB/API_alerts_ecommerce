from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    state = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    priceReal = models.DecimalField(max_digits=10, decimal_places=2)
    stars = models.IntegerField()
    enable = models.BooleanField()
    image = models.CharField(max_length=500)
    category = models.CharField(max_length=500)

class User(models.Model):
    name = models.CharField(max_length=500)
    lastname = models.CharField(max_length=500)
    mail = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)

class Historial (models.Model):
    id_HxP = models.IntegerField()



