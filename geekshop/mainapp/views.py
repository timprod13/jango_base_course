from django.shortcuts import render
from .models import Products, Category


def products(request):
    products = Products.objects.all()
    categories = Category.objects.all()
    context = {
        'title': 'каталог',
        'products': products,
        'categories': categories,

    }
    return render(request, 'mainapp/products.html', context)


def by_category(request, uuid):
    category = Category.objects.get(uuid=uuid)
    categories = Category.objects.all()
    products = Products.objects.filter(category=category)
    context = {
        'products': products,
        'category': category,
        'categories': categories,
    }
    return render(request, 'mainapp/by_category.html', context)
