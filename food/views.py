from django.shortcuts import render
from django.http import HttpResponse
from .models import item
from django.template import loader

# Create your views here.

def index(request):
    item_list = item.objects.all()
    template = loader.get_template('/templates/food/index.html')
    context = {
        'item_list': item_list,
    }
    return render(request, '/templates/food/index.html', context)

def item(request):
    return HttpResponse("Item page")

def detail(request, item_id):
    item = item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, '/templates/food/detail.html', context)
