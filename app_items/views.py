from django.shortcuts import render, get_object_or_404
from .models import Item


def item_view(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'item_detail.html', {'item': item})


def index(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})
