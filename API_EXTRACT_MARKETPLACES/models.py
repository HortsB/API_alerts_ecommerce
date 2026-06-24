from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Reservations(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    guest_count = models.IntegerField()
    reservations_time = models.DateTimeField(auto_now=True)
    comments = models.CharField(max_length=1000)