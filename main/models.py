from django.db import models

# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    power = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)