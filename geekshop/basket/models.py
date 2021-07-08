from django.conf import settings
from django.db import models
from mainapp.models import Products
from authapp.models import ShopUser


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='basket', verbose_name='пользователь', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='товар')
    quantity = models.PositiveSmallIntegerField(verbose_name='количество', default=0)
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='дата покупки')

    def __str__(self):
        return self.user
