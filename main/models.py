from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField(null=True)
    description = models.TextField()
    price = models.PositiveIntegerField(null=True)
    power = models.IntegerField(null=True)
    date_added = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)