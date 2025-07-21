from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.
def index(request):
    items_list = Item.objects.all()
    return HttpResponse(items_list)

def item(request):
    return HttpResponse("<h1>This is an item view</h2>")