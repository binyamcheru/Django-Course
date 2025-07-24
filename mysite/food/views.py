from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader

# Create your views here.
def index(request):
    items_list = Item.objects.all()
    # template = loader.get_template('food/index.html')
    context = {
        'items_list': items_list,
    }
    # return HttpResponse(template.render(context,request))
    return render(request,"food/index.html",context)

def item(request):
    return HttpResponse("<h1>This is an item view</h2>")

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item,
    }
    return render(request,"food/detail.html", context)