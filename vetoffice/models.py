from sqlite3 import Timestamp
from django.db import models

# Create your models here.

class Visits(models.Model):
    VisitId = models.AutoField(primary_key=True)
    CustomerName = models.CharField(max_length=500)

class Customers(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    CustomerName = models.CharField(max_length=500)
    CustomerAddress = models.CharField(max_length=500)
    CustomerPhone = models.CharField(max_length=500)
    DateOfJoining = models.DateField() 

class FB_N_01(models.Model):
    modelID = models.AutoField(primary_key=True)
    host = models.FloatField(null=True)
    actor = models.FloatField(null=True)
    road = models.FloatField(null=True)
    timestamp = models.DateField(null=True)

    def __str__(self):
        return self.modelID

class Red_Line_Tracking(models.Model):
    trackingID = models.AutoField(primary_key=True)
    combinedModelList = models.ForeignKey(FB_N_01, on_delete=models.CASCADE, related_name='combinedModelList')
    timestamp = models.DateField(null=True)

    def __str__(self):
        return self.trackingID

