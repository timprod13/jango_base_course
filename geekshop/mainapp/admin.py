from django.contrib import admin
from .models import Category, Products


class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated',)
    list_display_links = ('name',)


class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created', 'updated',)
    list_display_links = ('name',)


admin.site.register(Category, AdminCategory)
admin.site.register(Products, AdminProduct)
