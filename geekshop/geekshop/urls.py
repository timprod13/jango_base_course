from django.contrib import admin
from django.urls import path, include
from .views import index, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('products/', include('mainapp.urls', namespace='products'))
]
