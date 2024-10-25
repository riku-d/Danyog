from django.conf import settings
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name  

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='item_images/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)  # Assuming you have a default category
    quantity = models.PositiveIntegerField(default=1)  # Ensure you have this line for quantity
    

    def __str__(self):
        return self.name
