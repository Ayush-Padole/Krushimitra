from django.db import models
from django.db.models import CharField


class Cropsdetail(models.Model):
    cropname = models.CharField(max_length=500)
    season = models.CharField(max_length=500)
    soiltype = models.CharField(max_length=500)
    sowingmonth = models.CharField(max_length=500)
    harvestingmonth = models.CharField(max_length=500)
    fertilize = models.CharField(max_length=500)
    disease = models.CharField(max_length=500)
    crops = models.ImageField()

class Market_Price(models.Model):
    Cropname = models.CharField(max_length=500)
    Marketname = models.CharField(max_length=500)
    price = models.CharField(max_length=500)
    date = models.CharField(max_length=500)

class Farmers(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    village = models.CharField(max_length=100)
    taluka = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    problem = models.CharField(max_length=100)

class Government(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    link = models.CharField(max_length=500)

class Farmer_training(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=10)
    village = models.CharField(max_length=100)
    taluka = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    crop_detail = models.CharField(max_length=500)


class Newsupdate(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=1000)
    posted_date = models.DateField()





# Create your models here.
