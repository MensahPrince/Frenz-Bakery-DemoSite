from django.shortcuts import render
from .models import Product
# Create your views here.

def home(request):
    context={}
    return render(request, 'web/home.html', context)

def menu(request):
    context={}
    return render(request, 'web/menu.html', context)

def about(request):
    context={}
    return render(request, 'web/about.html', context)

def contact(request):
    context={}
    return render(request, 'web/contact.html', context)

def order(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'web/order.html', context)
