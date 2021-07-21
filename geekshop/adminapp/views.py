from audioop import reverse

from django.shortcuts import render, redirect

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404

from adminapp.forms import CreateCategoryForm, CreateProductForm
from authapp.forms import RegisterUser, EditUserForm
from authapp.models import ShopUser
from mainapp.models import Category, Products


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'админка/пользователи'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    content = {
        'title': title,
        'objects': users_list
    }

    return render(request, 'adminapp/users.html', content)


def user_create(request):
    title = 'пользователи/создание'

    if request.method == 'POST':
        user_form = RegisterUser(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect('/adminapp/users/read/')
    else:
        user_form = RegisterUser()

    content = {'title': title, 'update_form': user_form}

    return render(request, 'adminapp/user_update.html', content)


def user_update(request, pk):
    title = 'пользователи/редактирование'

    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        edit_form = EditUserForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('adminapp:user_update', args=[edit_user.pk]))
    else:
        edit_form = EditUserForm(instance=edit_user)

    content = {'title': title, 'update_form': edit_form}

    return render(request, 'adminapp/user_update.html', content)


def user_delete(request, pk):
    title = 'пользователи/удаление'

    user = get_object_or_404(ShopUser, pk=pk)
    user.delete()
    return HttpResponseRedirect('/adminapp/users/read/')


def categories(request):
    title = 'админка/категории'

    categories_list = Category.objects.all()

    content = {
        'title': title,
        'objects': categories_list
    }

    return render(request, 'adminapp/categories.html', content)


def category_create(request):
    title = 'создание категории'

    if request.method == 'POST':
        create_cat = CreateCategoryForm(request.POST, request.FILES)
        if create_cat.is_valid():
            create_cat.save()
            return HttpResponseRedirect('/adminapp/categories/read/')
    else:
        create_cat = CreateCategoryForm()

    content = {'title': title, 'create_cat': create_cat}

    return render(request, 'adminapp/category_create.html', content)


def category_update(request, pk):
    title = 'создание категории'
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        create_cat = CreateCategoryForm(request.POST, request.FILES, instance=category)
        if create_cat.is_valid():
            create_cat.save()
            return HttpResponseRedirect('/adminapp/categories/read/')
    else:
        create_cat = CreateCategoryForm(instance=category)

    content = {'title': title, 'create_cat': create_cat}

    return render(request, 'adminapp/category_create.html', content)


def category_delete(request, pk):
    title = 'удаление категории'
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return HttpResponseRedirect('/adminapp/categories/read/')


def products(request, pk):
    title = 'админка/продукт'

    category = get_object_or_404(Category, pk=pk)
    products_list = Products.objects.filter(category__pk=pk).order_by('name')
    products_list = Products.objects.filter(category__pk=pk).order_by('name')

    content = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', content)


def product_create(request, pk):
    title = 'админка/новый продукт'
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        create_prod = CreateProductForm(request.POST, request.FILES)
        if create_prod.is_valid():
            create_prod.save()
            return HttpResponseRedirect('/adminapp/categories/read/', )
    else:
        create_prod = CreateProductForm(initial={'category': category})

    content = {'title': title, 'create_prod': create_prod, 'category': category}

    return render(request, 'adminapp/product_create.html', content)


def product_read(request, pk):
    title = 'админка/о продукте'
    product = get_object_or_404(Products, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'adminapp/product_read.html', context)


def product_update(request, pk):
    title = 'админка/изменить продукт'
    product = get_object_or_404(Products, pk=pk)

    if request.method == 'POST':
        read_prod = CreateProductForm(request.POST, request.FILES, instance=product)
        if read_prod.is_valid():
            read_prod.save()
            return HttpResponseRedirect(f'/adminapp/products/read/category/{product.category.pk}/')
    else:
        read_prod = CreateProductForm(instance=product)

    content = {'title': title, 'create_prod': read_prod}

    return render(request, 'adminapp/product_create.html', content)


def product_delete(request, pk):
    title = 'админка/удалить продукт'
    product = get_object_or_404(Products, pk=pk)
    product.delete()
    return HttpResponseRedirect(f'/adminapp/products/read/category/{product.category.pk}/')
