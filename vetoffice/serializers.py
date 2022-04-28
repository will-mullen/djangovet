from rest_framework import serializers
from vetoffice.models import FB_N_01, Customers, Red_Line_Tracking, Visits

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customers
        fields=('CustomerID', 'CustomerName', 'CustomerAddress', 'CustomerPhone', 'DateOfJoining')

class VisitsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Visits
        fields=('VisitId', 'CustomerName')

class FB_N_01_Serializer(serializers.ModelSerializer):
    class Meta:
        model=FB_N_01
        # fields=('modelId', 'host', 'actor', 'road', 'timestamp')
        fields= '__all__'

class Red_Line_Tracking_Serializer(serializers.ModelSerializer):

    combinedModelList = FB_N_01_Serializer(many=True, read_only=True)

    class Meta:
        model=Red_Line_Tracking
        # fields=('trackingId', 'combinedModelList', 'timestamp')
        fields= '__all__'
