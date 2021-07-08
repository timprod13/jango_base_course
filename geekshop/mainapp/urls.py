from django.urls import path
from .views import products, by_category

app_name = 'products'
urlpatterns = [
    path('', products, name='index'),
    path('<int:pk>', by_category, name='by_category'),
]
