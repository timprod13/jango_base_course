from django.urls import path
from .views import basket, add_to_basket, remove_from_basket

app_name = 'basket'

urlpatterns = [
    path('', basket, name='index'),
    path('add/<int:pk>', add_to_basket, name='add_to_basket'),
    path('remove/<int:pk>', remove_from_basket, name='remove_from_basket'),
]