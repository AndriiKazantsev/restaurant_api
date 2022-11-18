from rest_framework import serializers
from .models import *

from django.contrib.auth.models import (
    Group
)


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = [
            'restaurant_id',
            'restaurant_name',
            'restaurant_cuisine',
            'restaurant_type'
        ]


class EmployeeSerializer(serializers.ModelSerializer):

    employee_id = serializers.CharField(read_only=True)

    class Meta:
        model = Employee
        fields = [
            'employee_id',
            'first_name',
            'last_name',
        ]


class ResultSerializer(serializers.ModelSerializer):

    restaurant = serializers.CharField(read_only=True)

    class Meta:
        model = Menu
        fields = [
            'restaurant_name',
            'menu_file',
            'uploaded_at'
        ]