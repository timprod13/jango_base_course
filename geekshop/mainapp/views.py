import random
from django.shortcuts import render, get_object_or_404
from basket.models import Basket
from .models import Products, Category
from basket.views import basket as bt


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Products.objects.all()

    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Products.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)

    return same_products[:3]


def product(request, pk):
    title = 'продукты'

    context = {
        'title': title,
        'links_menu': Category.objects.all(),
        'product': get_object_or_404(Products, pk=pk),
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product.html', context)


def products(request, pk=None):
    title = 'продукты/каталог'
    basket = get_basket(request.user)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    links_menu = Category.objects.all()
    products = Products.objects.all().order_by('price')

    if pk is not None:
        if pk == 0:
            products = Products.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(Category, pk=pk)
            products = Products.objects.filter(category__pk=pk).order_by('price')

        context = {
            'title': title,
            'links_menu': links_menu,
            'hot_product': hot_product,
            'same_products': same_products,
            'products': products,
            'category': category,
        }
        return render(request=request, template_name='mainapp/products.html', context=context)

    context = {
        'title': title,
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': same_products,
        'products': products,
        'basket': basket,
    }

    return render(request=request, template_name='mainapp/products.html', context=context)
