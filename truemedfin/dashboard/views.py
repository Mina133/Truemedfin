from django.shortcuts import render
from .models import Item, List
from django.views.generic import ListView
# Create your views here.

class ItemView(ListView):
    model = Item
    template_name = 'items.html'
    context_object_name = 'items'

class ListView(ListView):
    model = List
    template_name = 'lists.html'
    context_object_name = 'lists'