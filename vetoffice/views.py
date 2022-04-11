from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from vetoffice.models import Customers, Visits
from vetoffice.serializers import CustomersSerializer, VisitsSerializer

# def home(request):
#   context = {"name": "Spot"}
#   return render(request, 'vetoffice/home.html', context)

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





