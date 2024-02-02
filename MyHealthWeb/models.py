from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    bg = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)

    