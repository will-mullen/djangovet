from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from vetoffice.models import Customers, Visits
from vetoffice.serializers import CustomersSerializer, FB_N_01_Serializer, Red_Line_Tracking_Serializer, VisitsSerializer

def home(request):
  context = {"name": "Spot"}
  return render(request, 'vetoffice/home.html', context)

@csrf_exempt
def customersApi(request, id=0):
    if request.method=='GET':
        customers = Customers.objects.all()
        customers_serializer = CustomersSerializer(customers,many=True)
        return JsonResponse(customers_serializer.data,safe=False)
    elif request.method=='POST':
        customers_data = JSONParser().parse(request)
        customers_serializer = CustomersSerializer(data=customers_data)
        if customers_serializer.is_valid():
            customers_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Faled to Add",safe=False)
    elif request.method=='PUT':
        customers_data = JSONParser().parse(request)
        customers=Customers.objects.get(CustomerId=customers_data['CustomerId'])
        customers_serializer = CustomersSerializer(customers,data=customers_data)
        if customers_serializer.is_valid():
            customers_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        customers= Customers.objects.get(CustomerID=id)
        customers.delete()
        return JsonResponse("Deleted Successfully", safe=False)
        
@csrf_exempt
def FB_N_01_Api(request, id=0):
    if request.method=='GET':
        FB_N_01 = FB_N_01.objects.all()
        FB_N_01_serializer = FB_N_01_Serializer(FB_N_01,many=True)
        return JsonResponse(FB_N_01_serializer.data,safe=False)
    elif request.method=='POST':
        FB_N_01_data = JSONParser().parse(request)
        FB_N_01_serializer = FB_N_01_Serializer(data=FB_N_01_data)
        if FB_N_01_serializer.is_valid():
            FB_N_01_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Faled to Add",safe=False)
    elif request.method=='PUT':
        FB_N_01_data = JSONParser().parse(request)
        FB_N_01=FB_N_01.objects.get(modelId=FB_N_01_data['modelId'])
        FB_N_01_serializer = FB_N_01_Serializer(FB_N_01,data=FB_N_01_data)
        if FB_N_01_serializer.is_valid():
            FB_N_01_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        FB_N_01= FB_N_01.objects.get(modelID=id)
        FB_N_01.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def Red_Line_Tracking_Api(request, id=0):
    if request.method=='GET':
        Red_Line_Tracking = Red_Line_Tracking.objects.all()
        Red_Line_Tracking_serializer = Red_Line_Tracking_Serializer(Red_Line_Tracking,many=True)
        return JsonResponse(Red_Line_Tracking_serializer.data,safe=False)
    elif request.method=='POST':
        Red_Line_Tracking_data = JSONParser().parse(request)
        Red_Line_Tracking_serializer = Red_Line_Tracking_Serializer(data=Red_Line_Tracking_data)
        if Red_Line_Tracking_serializer.is_valid():
            Red_Line_Tracking_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Faled to Add",safe=False)
    elif request.method=='PUT':
        Red_Line_Tracking_data = JSONParser().parse(request)
        Red_Line_Tracking=Red_Line_Tracking.objects.get(modelId=Red_Line_Tracking_data['trackingId'])
        Red_Line_Tracking_serializer = Red_Line_Tracking_Serializer(Red_Line_Tracking,data=Red_Line_Tracking_data)
        if Red_Line_Tracking_serializer.is_valid():
            Red_Line_Tracking_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        Red_Line_Tracking= Red_Line_Tracking.objects.get(modelID=id)
        Red_Line_Tracking.delete()
        return JsonResponse("Deleted Successfully", safe=False)




