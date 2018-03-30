from django.db import models


# Create your models here.
class Stock(models.Model):
    ticker = models.CharField(max_length=50)
    high = models.FloatField(blank=True, default=0)
    low = models.FloatField(blank=True, default=0)
    opening = models.FloatField(blank=True, default=0)
    closing = models.FloatField(blank=True, default=0)
    volume = models.IntegerField(blank=True, default=0)
    date = models.DateField(blank=True, null=True)


class Prediction(models.Model):
    ticker = models.CharField(max_length=50)
    prediction = models.FloatField(blank=True, default=0)
    date_ran_experiment = models.DateField(blank=True, null=True)


class Company(models.Model): 
    ticker = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100, unique=True)
    exchange = models.CharField(max_length=100) 
