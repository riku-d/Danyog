from django.shortcuts import render, get_object_or_404, redirect
from .forms import ItemForm
from .models import Item, Category  # Import Category model if you have it
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from shop.models import Order,DeliveryProof

@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user  # Attach the item to the logged-in user
            item.save()
            messages.success(request, 'Item added successfully!')
            return redirect('listitem:item_list')
    else:
        form = ItemForm()
    
    return render(request, 'listitem/add_item.html', {'form': form})

@login_required
def item_list(request):
    if request.user.is_authenticated:
        items = Item.objects.filter(user=request.user)  # Show only items added by this user
    else:
        items = Item.objects.none()  # Anonymous users should not see items

    selected_category = request.GET.get('category', '')

    if selected_category:
        items = items.filter(category__name=selected_category)  # Filter by selected category

    categories = Category.objects.all()  # Get all categories for the dropdown

    # Fetch orders for items that belong to the current user
    orders = Order.objects.filter(item__in=items)

    # Fetch delivery proofs submitted by orphanages for these orders
    proofs = DeliveryProof.objects.filter(order__in=orders)

    return render(request, 'listitem/item_list.html', {
        'items': items,
        'categories': categories,
        'selected_category': selected_category,
        'proofs': proofs,  # Pass proofs to the template
    })



@login_required
def update_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)  # user=request.user Ensure the user owns the item
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item updated successfully!')
            return redirect('listitem:item_list')
    else:
        form = ItemForm(instance=item)
    
    return render(request, 'listitem/update_item.html', {'form': form, 'item': item})

@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)  # This will raise a 404 if the item doesn't exist
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Item deleted successfully!')
        return redirect('listitem:item_list')  # Redirect after deletion
    return render(request, 'listitem/delete_item.html', {'item': item})

def category_products(request, category_name):
    # Fetch items that match the category name
    products = Item.objects.filter(category__name__iexact=category_name)
    
    # Pass the products and the category name to the template
    context = {
        'products': products,
        'category_name': category_name,
    }
    return render(request, 'listitem/category_products.html', context)
