from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import json, os
from authapp.models import ShopUser
from mainapp.models import Category, Products

JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')

        Category.objects.all().delete()
        for category in categories:
            new_category = Category(**category)
            new_category.save()

        products = load_from_json('products')

        Products.objects.all().delete()
        for product in products:
            category_name = product["category"]
            _category = Category.objects.get(name=category_name)
            product['category'] = _category
            new_product = Products(**product)
            new_product.save()

        super_user = ShopUser.objects.create_superuser('timprod', 'timoha_defn@mail.ru', 'admin', age=27)
