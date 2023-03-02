import datetime

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from app_users.forms import AuthForm, RegisterForm
from django.contrib.auth.views import LoginView


def login_view(request):
    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            user_name = auth_form.cleaned_data['user_name']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=user_name, password=password)
            if user:
                if user.is_superuser:
                    auth_form.add_error('__all__', 'Ошибка! Вы являетесь администратором!')
                elif user.is_active:
                    time = datetime.datetime.now().time().hour
                    if 8 > time or time > 22:
                        auth_form.add_error('__all__', 'Ошибка! Сайт спит с 22 до 8')
                    else:
                        login(request, user)
                        return HttpResponse('Вы успешно вошли в систему')
                else:
                    auth_form.add_error('__all__', 'Ошибка! Учетная записть пользователя не активна!')

            else:
                auth_form.add_error('__all__', 'Ошибка! Проверьте написания логина и пароля!')

    else:
        auth_form = AuthForm()
    context = {
        'form': auth_form
    }

    return render(request, 'app_users/login.html', context=context)


class AnotherLoginView(LoginView):
    template_name = 'app_users/login.html'


class MainView(View):
    def get(self, request):
        return render(request, template_name='main.html')


def logout_view(request):
    logout(request)
    return HttpResponse('Вы успешно вышли из своей учетной записи!')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user_name, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'app_users/register.html', {'form': form})


def account_view(request):
    return render(request, template_name='app_users/account.html')
