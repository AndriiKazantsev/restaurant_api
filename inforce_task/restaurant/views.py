from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import *
from .serializers import *
from django.core.files.storage import default_storage

# Create your views here.


@csrf_exempt
def restaurantApi(request, id=0):
    if request.method == 'GET':
        restaurant = Restaurant.objects.all()
        restaurants_serializer = RestaurantSerializer(restaurant, many=True)
        return JsonResponse(restaurants_serializer.data, safe=False)
    elif request.method == 'POST':
        restaurant_data = JSONParser().parse(request)
        restaurants_serializer = RestaurantSerializer(data=restaurant_data)
        if restaurants_serializer.is_valid():
            restaurants_serializer.save()
            return JsonResponse("Added succesfully", safe=False)
        return JsonResponse("Failed to add a record", safe=False)
    elif request.method == 'PUT':
        restaurant_data = JSONParser().parse(request)
        restaurant = Restaurant.objects.get(restaurant_name=restaurant_data['restaurant_name'])
        restaurant_serializer = RestaurantSerializer(restaurant, data=restaurant_data)
        if restaurant_serializer.is_valid():
            restaurant_serializer.save()
            return JsonResponse("Updated succesfully", safe=False)
    elif request.method == 'DELETE':
        restaurant_data = JSONParser().parse(request)
        restaurant = Restaurant.objects.get(restaurant_name=restaurant_data['restaurant_name'])
        restaurant.delete()
        return JsonResponse("Deleted succesfully", safe=False)


@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employees = Employee.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(EmployeeId=employee_data['EmployeeId'])
        employees_serializer = EmployeeSerializer(employee, data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        employee = Employee.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def uploadMenu(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
