from django.urls import path
from .views import basket, add_to_basket, basket_remove

app_name = 'basket'

urlpatterns = [
    path('', basket, name='index'),
    path('add/<int:pk>', add_to_basket, name='add_to_basket'),
    path('remove/<int:pk>', basket_remove, name='basket_remove'),
]