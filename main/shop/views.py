# shop/views.py

from django.shortcuts import render, get_object_or_404,redirect
from listitem.models import Item  # Assuming 'Item' is your model in the listitem app
from .models import Cart, CartItem
from .models import Order, DeliveryProof
from django.contrib import messages
from django.core.mail import send_mail

def shop_grid(request):
    # Get search query from the URL parameters
    search_query = request.GET.get('category', '')

    # Filter items by the selected category, or show all items if no category is selected
    if search_query:
        all_items = Item.objects.filter(category__name=search_query)
    else:
        all_items = Item.objects.all()

    # Fetch the latest 6 items for "New Arrivals"
    new_items = Item.objects.order_by('-id')[:6]

    # Pass context to the template
    context = {
        'all_items': all_items,
        'search_query': search_query,  # Pass the selected category back to the template
        'new_items': new_items,  # Add new_items for the "New Arrivals" section
    }

    
    return render(request, 'shop/shop-grid.html', context)


def shop_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)  # Fetch the specific item
    context = {
        'item': item,  # Pass the item to the template
    }
    return render(request, 'shop/shop-details.html', context)

def shoping_cart(request):
    return render(request, 'shop/shoping-cart.html')

def checkout(request):
    if request.user.is_authenticated:
        # Fetch the cart and cart items for authenticated users
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
    else:
        # Session-based cart for anonymous users
        session_cart = request.session.get('cart', {})
        cart_items = []
        for item_id, quantity in session_cart.items():
            item = get_object_or_404(Item, id=item_id)
            cart_items.append({
                'item': item,
                'quantity': quantity
            })

    return render(request, 'shop/checkout.html', {
        'cart_items': cart_items
    })

def contact(request):
    return render(request, 'shop/contact.html')

def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.user.is_authenticated:
        # For authenticated users, use the user cart
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
        if not created:
            cart_item.quantity += 1
        cart_item.save()
    else:
        # For anonymous users, use session-based cart
        cart = request.session.get('cart', {})
        print("Cart before:", cart)  # Debugging statement
        
        # Update cart
        cart[str(item_id)] = cart.get(str(item_id), 0) + 1
        
        # Debugging statement
        print(f"Added item {item_id}, Cart now:", cart)
        
        # Save the updated cart back to session
        request.session['cart'] = cart
        request.session.modified = True
        print("Session modified:", request.session.modified)  # Should print 'True'

    return redirect('view_cart')





def view_cart(request):
    if request.user.is_authenticated:
        # For authenticated users, fetch the user cart
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
    else:
        # For anonymous users, use session-based cart
        session_cart = request.session.get('cart', {})
        cart_items = []
        for item_id, quantity in session_cart.items():
            item = get_object_or_404(Item, id=item_id)
            cart_items.append({
                'item': item,
                'quantity': quantity
            })

    return render(request, 'shop/view_cart.html', {
        'cart': cart if request.user.is_authenticated else None,
        'cart_items': cart_items
    })





def remove_from_cart(request, item_id):
    if request.user.is_authenticated:
        # For authenticated users, remove the item from the user's cart in the database
        cart = Cart.objects.get(user=request.user)
        cart_item = get_object_or_404(CartItem, cart=cart, item_id=item_id)
        cart_item.delete()
    else:
        # For anonymous users, remove the item from the session-based cart
        session_cart = request.session.get('cart', {})
        if str(item_id) in session_cart:
            del session_cart[str(item_id)]  # Remove the item from the session cart
            request.session['cart'] = session_cart  # Update the session

    return redirect('view_cart')


def place_order(request):
    if request.method == 'POST':
        # Handle the order submission logic here (e.g., create an order, deduct stock, etc.)
        # Assuming order gets created with user and orphanage info
        order = Order.objects.create(user=request.user, orphanage=request.user.orphanage)

        # Redirect to the confirmation page after placing the order
        messages.success(request, 'Order placed successfully. Please provide proof of delivery once received.')
        return redirect('order_confirmation', order_id=order.id)

    return redirect('checkout')

def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    
    if request.method == 'POST':
        # Handle proof submission
        image = request.FILES['proof_image']
        review = request.POST['review']
        DeliveryProof.objects.create(order=order, image=image, review=review)
        
        messages.success(request, 'Proof of delivery submitted successfully.')
        # Notify the user that their listed item has been delivered
        # (You would implement a notification system here, e.g., via email or in-app notifications)
        return redirect('user_order_notification', order_id=order.id)

    return render(request, 'shop/order_confirmation.html', {'order': order})

def notify_user_of_delivery(order):
    send_mail(
        'Your item has been delivered!',
        f'Hi {order.user.username}, the orphanage has confirmed the delivery of the item "{order.item.name}".',
        'from@example.com',
        [order.user.email],
        fail_silently=False,
    )






def place_order(request):
    if request.method == 'POST':
        cart_items = CartItem.objects.filter(cart__user=request.user)

        if cart_items.exists():
            for cart_item in cart_items:
                order = Order.objects.create(
                    user=request.user,
                    orphanage=request.user,  # assuming orphanage is the logged-in user
                    item=cart_item.item,
                    
                    first_name = request.POST.get('first_name'),
                    last_name = request.POST.get('last_name'),
                    country = request.POST.get('country'),
                    address = request.POST.get('address'),
                    address2 = request.POST.get('address2', ''),  # Optional
                    city = request.POST.get('city'),
                    state = request.POST.get('state'),
                    postcode = request.POST.get('postcode'),
                    phone = request.POST.get('phone'),
                    email = request.POST.get('email'),
                    order_notes = request.POST.get('order_notes', ''),
                )
                # Save the order and clear the cart
                cart_item.delete()
            

            # Redirect to order confirmation page
            return redirect('order_confirmation', order_id=order.id)  # Redirect to a confirmation page

        else:
            # Handle case where there are no items in the cart
            return redirect('view_cart')  # Redirect back to cart if empty

    return redirect('checkout')  # Redirect to checkout if the request is not POST

def order_list(request):
    orders = Order.objects.filter(orphanage=request.user)
    return render(request, 'shop/order_list.html', {'orders': orders})
     
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, orphanage=request.user)  # Check that the orphanage owns the order
    return render(request, 'shop/order_detail.html', {'order': order})