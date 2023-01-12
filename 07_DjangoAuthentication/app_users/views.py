import datetime

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from app_users.forms import AuthForm
from django.contrib.auth.views import LoginView, LogoutView


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

    return render(request, 'users/login.html', context=context)


class AnotherLoginView(LoginView):
    template_name = 'users/login.html'


class MainView(View):
    def get(self, request):
        return render(request, template_name='main.html')


def logout_view(request):
    logout(request)
    return HttpResponse('Вы успешно вышли из своей учетной записи!')

