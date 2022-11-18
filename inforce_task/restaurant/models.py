from django.db import models
import uuid

# Create your models here.


class Restaurant(models.Model):
    """Model representing a restaurant."""
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=200, null=True, blank=True)
    restaurant_cuisine = models.CharField(max_length=100, null=True, blank=True)
    restaurant_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.restaurant_name


class Employee(models.Model):
    """Model representing an employee."""
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, null=True, blank=True,)
    last_name = models.CharField(max_length=100, null=True, blank=True,)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['last_name', 'first_name']


class Menu(models.Model):
    """Model representing a menu."""
    restaurant_name = models.ForeignKey(Restaurant, null=True, blank=True, on_delete=models.CASCADE)
    menu_file = models.FileField(upload_to='menus/', default=None, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.restaurant_name.name
