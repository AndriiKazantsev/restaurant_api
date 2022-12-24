from django.contrib import admin
from .models import *

# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'employee_id',
        'first_name',
        'last_name'
    )


class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        'restaurant_id',
        'restaurant_name',
        'restaurant_cuisine',
        'restaurant_type'
    )


class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'restaurant_name',
        'menu_file',
        'uploaded_at'
    )


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Menu, MenuAdmin)
