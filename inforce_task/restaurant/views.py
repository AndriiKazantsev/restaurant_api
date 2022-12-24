from rest_framework import generics
from .serializers import *

from django.core.files.storage import default_storage

# Create your views here.


class RestaurantList(generics.ListCreateAPIView):
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        queryset = Restaurant.objects.all()
        restaurant_name = self.request.query_params.get('restaurant_name')
        if restaurant_name is not None:
            queryset = queryset.filter(restaurantName=restaurant_name)
        return queryset


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()


class EmployeeList(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
