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
        fields=('ModelID', 'Host', 'Actor', 'Road', 'Timestamp')
        # fields= '__all__'

class Red_Line_Tracking_Serializer(serializers.ModelSerializer):

    CombinedModelList = FB_N_01_Serializer(many=True, read_only=True)

    class Meta:
        model=Red_Line_Tracking
        fields=('TrackingID', 'CombinedModelList', 'Timestamp')
        depth = 1
        # fields= '__all__'
