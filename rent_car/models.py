from django.db import models
import datetime


# Create your models here.
class CarBrand(models.Model): 
    name = models.CharField(max_length=30)
    status = models.BooleanField(default=True)


class CarModel(models.Model):
    name = models.CharField(max_length=50)
    brand = models.IntegerField()
    status = models.BooleanField(default=True)


class CarType(models.Model):
    type = models.CharField(max_length=20)
    model = models.IntegerField()
    status = models.BooleanField(default=True)


class CarOrders(models.Model):
    brand = models.IntegerField()
    model = models.IntegerField()
    type = models.IntegerField()
    date_request = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=True)
    date_from = models.DateField()
    date_to = models.DateField()