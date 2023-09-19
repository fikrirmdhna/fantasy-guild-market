from django.db import models

# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField(null=True)
    power = models.IntegerField(null=True)
    date_added = models.DateField(auto_now_add=True)