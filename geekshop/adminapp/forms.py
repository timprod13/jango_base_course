from django.forms import ModelForm
from mainapp.models import Category, Products


class CreateCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name', )


class CreateProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ('name', 'description', 'price', 'image', 'category',)
