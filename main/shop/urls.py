from django.urls import path
from .views import shop_grid,shop_detail,checkout,shoping_cart,contact,add_to_cart,view_cart,remove_from_cart,checkout,place_order,order_confirmation,order_list, order_detail

urlpatterns = [
    path('', shop_grid, name='shop_grid'),
    # path('shop-details', shop_detail, name='shop_detail'),
    path('shop-details/<int:item_id>/', shop_detail, name='shop_detail'),
    path('shoping-cart', shoping_cart, name='shoping_cart'),
    path('checkout', checkout, name='checkout'),
    path('contact', contact, name='contact'),

    path('add-to-cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('remove-from-cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('order/confirmation/<int:order_id>/', order_confirmation, name='order_confirmation'),
    path('place-order/',place_order, name='place_order'),
    path('orders/', order_list, name='order_list'),
    path('orders/<int:order_id>/', order_detail, name='order_detail'),
    
]
