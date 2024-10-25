from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('user', 'User'),
        ('orphanage', 'Orphanage'),
    )
    name = models.CharField(max_length=255, default="Default Name")  # Default value for name
    mobile_number = models.CharField(max_length=15)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

