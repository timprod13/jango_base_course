from django.contrib.auth.models import AbstractUser
from django.db import models


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatar', blank=True, verbose_name='avatar')
    age = models.PositiveSmallIntegerField(verbose_name='age', blank=True)
