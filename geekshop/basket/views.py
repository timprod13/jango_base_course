from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from mainapp.models import Products, Category
from .models import Basket


def basket(request):
    total = 0
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        total = sum([i.quantity * i.product.price for i in basket])
    title = 'корзина'

    context = {
        'title': title,
        'basket': basket,
        'total': total,
    }
    return render(request, 'basket/basket.html', context)


def add_to_basket(request, pk):
    product = get_object_or_404(Products, pk=pk)

    basket = Basket.objects.filter(user=request.user, product=product).first()
    if not basket:
        basket = Basket(user=request.user, product=product)
    basket.quantity += 1
    basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def remove_from_basket(request, pk):
    pass
