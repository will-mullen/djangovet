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
    ModelID = models.AutoField(primary_key=True)
    Host = models.FloatField()
    Actor = models.FloatField()
    Road = models.FloatField()
    Timestamp = models.DateField()

    def __str__(self):
        return self.modelID

class Red_Line_Tracking(models.Model):
    TrackingID = models.AutoField(primary_key=True)
    # CombinedModelList = models.ForeignKey(FB_N_01, default= None, on_delete=models.CASCADE, related_name='CombinedModelList')
    CombinedModelList = models.ManyToManyField(FB_N_01)
    Timestamp = models.DateField()

    def __str__(self):
        return self.trackingID

class Tracking1(models.Model):
    name = models.CharField(max_length=10)

class Model1(models.Model):
    name = models.CharField(max_length=10)
    modelid = models.ManyToManyField(Tracking1)

    def __str__(self):
        return self.name

