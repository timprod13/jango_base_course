from django.shortcuts import render
from .models import Products, Category


def products(request):
    links = [
        {'href': 'product_all', 'name': 'все'},
        {'href': 'product_classic', 'name': 'классика'},
        {'href': 'product_home', 'name': 'дом'},
        {'href': 'product_modern', 'name': 'модерн'},
        {'href': 'product_office', 'name': 'офис'}
    ]

    products = Products.objects.all()
    categories = Category.objects.all()
    context = {
        'title': 'каталог',
        'links': links,
        'products': products,
        'categories': categories,

    }
    return render(request, 'products.html', context)


def by_category(request, uuid):
    category = Category.objects.get(uuid=uuid)
    products = Products.objects.filter(category=category)
    context = {
        'products': products,
        'category': category,
    }
    return render(request, 'by_category.html', context)
