from django.urls import path
from . import views

app_name = 'listitem'

urlpatterns = [
    path('add/', views.add_item, name='add_item'),
    path('items/', views.item_list, name='item_list'),
    path('update/<int:item_id>/', views.update_item, name='update_item'),
    # path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('listitem/items/', views.item_list, name='item_list'),  # This should match
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),

    path('category/<str:category_name>/', views.category_products, name='category_products'),

    


    
]
