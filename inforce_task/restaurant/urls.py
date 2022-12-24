from django.urls import re_path
from .views import *

urlpatterns = [
    re_path('restaurant/', RestaurantList.as_view()),
    re_path('restaurant/<int:pk>/', RestaurantDetail.as_view()),

    re_path('employee/', EmployeeList.as_view()),
    re_path('employee/<int:pk>/', EmployeeDetail.as_view()),

    # re_path(r'^employee/uploadmenu', views.uploadMenu),
]
