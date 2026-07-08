from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    state = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    priceReal = models.DecimalField(max_digits=10, decimal_places=2)
    stars = models.DecimalField(max_digits=3, decimal_places=2)
    enable = models.BooleanField()
    image = models.CharField(max_length=500)
    category = models.CharField(max_length=500)

class Category(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()

class ProductState(models.Model):
    name = models.CharField(max_length=500)
class User(models.Model):
    name = models.CharField(max_length=500)
    lastname = models.CharField(max_length=500)
    mail = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    historial = models.ForeignKey('Historial',null=True, blank=True, on_delete=models.CASCADE)

class Historial (models.Model):
    id_HxP = models.ForeignKey('Product', on_delete=models.CASCADE)

class HistorialProduct(models.Model):
    id_HxP = models.ForeignKey('Historial', on_delete=models.CASCADE)
    id_Product = models.ForeignKey('Product', on_delete=models.CASCADE)
    date_viewed = models.DateTimeField(auto_now_add=True)
    marked_as_favorite = models.BooleanField(default=False)

class Alert(models.Model):
    id_HxP = models.ForeignKey('Historial', on_delete=models.CASCADE)
    id_User = models.ForeignKey('User', on_delete=models.CASCADE)
    alert = models.CharField(max_length=500)




