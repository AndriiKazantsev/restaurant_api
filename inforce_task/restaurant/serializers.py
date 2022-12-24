from rest_framework import serializers
from .models import *


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


class UploadMenuSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        menu = Menu(
            restaurant=validated_data['restaurant'],
            menu_file=validated_data['file'],
            uploaded_at=validated_data['uploaded_by']
        )
        menu.save()
        return menu

    class Meta:
        fields = [
            'restaurant',
            'menu_file',
            'uploaded_at'

        ]
        model = Menu