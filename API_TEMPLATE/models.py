from django.db import models

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class User(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class ProductState(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    p_state = models.ForeignKey('ProductState', on_delete=models.CASCADE)
    stars = models.IntegerField()
    realPrice = models.DecimalField(max_digits=10, decimal_places=2)
    discountPrice = models.DecimalField(max_digits=10, decimal_places=2)
    enabled = models.BooleanField(default=True)
    image = models.ImageField(upload_to='product_images/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    discountPercentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name,self.description

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.instrument}"
    
class Album(models.Model):
    musician = models.ForeignKey
    