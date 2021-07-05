import uuid as uuid
from django.db import models


class Category(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, verbose_name='uuid')
    name = models.CharField(max_length=100, verbose_name='категория')
    created = models.DateField(auto_now_add=True, verbose_name='дата создания')
    updated = models.DateField(auto_now=True, verbose_name='дата изменения')

    class Meta:
        ordering = ['name']
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Products(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, verbose_name='uuid')
    name = models.CharField(max_length=100, verbose_name='продукт')
    description = models.TextField(blank=True, verbose_name='описание')
    price = models.DecimalField(max_digits=1000000, decimal_places=2, verbose_name='цена')
    image = models.ImageField(upload_to='products', verbose_name='изображение')
    created = models.DateField(auto_now_add=True, verbose_name='дата создания')
    updated = models.DateField(auto_now=True, verbose_name='дата изменения')
    category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return self.name
