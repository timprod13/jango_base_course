from django.urls import path
from .views import login, logout, registration, edit

app_name = 'auth'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('registration/', registration, name='registration'),
    path('edit/', edit, name='edit'),
]