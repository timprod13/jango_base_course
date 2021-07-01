from django.shortcuts import render


def products(request):
    links = [
        {'href': 'product_all', 'name': 'все'},
        {'href': 'product_classic', 'name': 'классика'},
        {'href': 'product_home', 'name': 'дом'},
        {'href': 'product_modern', 'name': 'модерн'},
        {'href': 'product_office', 'name': 'офис'}
    ]

    context = {
        'title': 'каталог',
        'links': links
    }

    return render(request, 'products.html', context)
