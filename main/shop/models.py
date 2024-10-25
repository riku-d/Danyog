from django.conf import settings
from django.db import models
from listitem.models import Item  # Assuming your items are in the 'listitem' app
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    items = models.ManyToManyField(Item, through='CartItem')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart {self.id} for {self.user}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"
    
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    orphanage = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='orphanage_orders', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    
    # New fields with default values
    first_name = models.CharField(max_length=50, default='First')
    last_name = models.CharField(max_length=50, default='Last')
    country = models.CharField(max_length=100, default='Country')
    address = models.CharField(max_length=255, default='Address')
    address2 = models.CharField(max_length=255, blank=True, default='')  # Optional
    city = models.CharField(max_length=100, default='City')
    state = models.CharField(max_length=100, default='State')
    postcode = models.CharField(max_length=20, default='000000')
    phone = models.CharField(max_length=20, default='0000000000')
    email = models.EmailField(default='example@example.com')
    order_notes = models.TextField(blank=True, default='')  # Optional

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} by {self.user}"

class DeliveryProof(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='delivery_proofs/')
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
