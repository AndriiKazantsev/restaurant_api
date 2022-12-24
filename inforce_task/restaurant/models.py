from django.db import models
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError("Users must have a username")
        if email is None:
            raise TypeError("Users must have an email")
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError("Superusers must have a password.")

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        """ Строковое представление модели (отображается в консоли) """
        return self.email

    @property
    def token(self):

        return self._generate_jwt_token()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')


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
    menu_name = models.CharField(max_length=100,null=True, default=None, blank=True)
    restaurant_name = models.ForeignKey(Restaurant, null=True, blank=True, on_delete=models.CASCADE)
    menu_file = models.FileField(upload_to='static/upload', default=None, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.menu_name
