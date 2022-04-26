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

