from basket.models import Basket
from django.shortcuts import render, get_object_or_404
from .models import Products, Category


def products(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    products = Products.objects.all()
    categories = Category.objects.all()
    context = {
        'title': 'каталог',
        'products': products[:3],
        'categories': categories,
        'basket': basket,
    }
    return render(request, 'mainapp/products.html', context)


def by_category(request, pk=None):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    categories = Category.objects.all()
    if pk == 0:
        products = Products.objects.all()
        category = {'name': 'все'}
        context = {
            'products': products,
            'category': category,
            'categories': categories,
            'basket': basket,
        }
        return render(request, 'mainapp/by_category.html', context)

    category = get_object_or_404(Category, pk=pk)

    products = Products.objects.filter(category__pk=pk)
    context = {
        'products': products,
        'category': category,
        'categories': categories,
        'basket': basket,
    }
    return render(request, 'mainapp/by_category.html', context)
