from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^restaurant$', views.restaurantApi),
    re_path(r'^restaurant/([0-9]+)$', views.restaurantApi),

    re_path(r'^employee$', views.employeeApi),
    re_path(r'^employee/([0-9]+)$', views.employeeApi),

    re_path(r'^employee/uploadmenu', views.uploadMenu)
]
