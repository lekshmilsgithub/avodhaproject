from django.http import HttpResponse
from django.shortcuts import render
from .models import shop


# Create your views here.
def avodha(request):
    product = shop.objects.all()
    return render(request, "home.html", {'products': product})


def detail(request, shop_id):
    product1 = shop.objects.get(id=shop_id)
    return render(request, "detail.html", {'product': product1


def add_product(request):
    return render(request, "add_product.html")
