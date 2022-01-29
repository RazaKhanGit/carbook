from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    car_no = models.TextField(unique=True)
    car_name = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now=True)

    