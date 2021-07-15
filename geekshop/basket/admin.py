from django.contrib import admin
from .models import Basket


class AdminBasket(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity',)


admin.site.register(Basket, AdminBasket)
