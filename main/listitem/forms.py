from django import forms
from .models import Item, Category

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'image', 'category', 'quantity']  # Add new fields
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter item name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter item description'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter item quantity'}),
            'category': forms.Select(attrs={'class': 'form-control'}),  # Dropdown for categories
        }
