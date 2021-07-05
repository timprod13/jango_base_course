from django.contrib import admin
from .models import ShopUser


class AdminShopUser(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'age',)
    list_display_links = ('username',)


admin.site.register(ShopUser, AdminShopUser)
