from django.core.management import BaseCommand
from authapp.models import ShopUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        super_user = ShopUser.objects.create_superuser('new_timprod', 'timprod@mail.ru', 'new_admin', age=27)
