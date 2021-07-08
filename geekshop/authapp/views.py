from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import LoginForm, EditUserForm, RegisterUser
from django.contrib import auth
from django.urls import reverse
from .models import ShopUser


def login(request):
    title = 'вход'

    login_form = LoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))

    content = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def edit(request):
    title = 'редактирование'

    if request.method == 'POST':
        edit_form = EditUserForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = EditUserForm(instance=request.user)

    content = {'title': title, 'edit_form': edit_form}

    return render(request, 'authapp/user_edit.html', content)


def registration(request):
    title = 'регистрация'

    if request.method == 'POST':
        reg_form = RegisterUser(request.POST, request.FILES)
        if reg_form.is_valid():
            reg_form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        reg_form = RegisterUser()
    content = {'title': title, 'reg_form': reg_form}
    return render(request, 'authapp/registration.html', content)