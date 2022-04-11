from rest_framework import serializers
from vetoffice.models import Customers, Visits

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customers
        fields=('CustomerID', 'CustomerName', 'CustomerAddress', 'CustomerPhone', 'DateOfJoining')

class VisitsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Visits
        fields=('VisitId', 'CustomerName')