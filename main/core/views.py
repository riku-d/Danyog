# core/views.py

from django.shortcuts import render
from listitem.models import Item

def index(request):
    # Get the search query (category) from the request
    query = request.GET.get('category', None)
    
    # Filter items by the selected category if provided, else show all items
    if query:
        all_items = Item.objects.filter(category__name__iexact=query)
    else:
        all_items = Item.objects.all()
    
    context = {
        'all_items': all_items,            # Pass the items (filtered or not)
        'search_query': query,             # Pass the selected category
    }
    return render(request, 'core/index.html', context)

def about(request):
    return render(request, 'core/about.html')
