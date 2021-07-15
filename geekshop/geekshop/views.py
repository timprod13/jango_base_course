from django.shortcuts import render
from basket.models import Basket


def index(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    context = {
        'title': 'магазин',
        'basket': basket,
    }
    return render(request, 'geekshop/index.html', context)


def contact(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    context = {
        'title': 'контакты',
        'basket': basket,
    }
    return render(request, 'geekshop/contact.html', context)
