from django.conf import settings
from django.db import models
from mainapp.models import Products
from authapp.models import ShopUser


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='basket', verbose_name='пользователь',
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='товар')
    quantity = models.PositiveSmallIntegerField(verbose_name='количество', default=0)
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='дата покупки')

    def __str__(self):
        return self.user


@property
def product_cost(self):
    "return cost of all products this type"
    return self.product.price * self.quantity


@property
def total_quantity(self):
    "return total quantity for user"
    _items = Basket.objects.filter(user=self.user)
    _totalquantity = sum(list(map(lambda x: x.quantity, _items)))
    return _totalquantity


@property
def total_cost(self):
    "return total cost for user"
    _items = Basket.objects.filter(user=self.user)
    _totalcost = sum(list(map(lambda x: x.product_cost, _items)))
    return _totalcost
