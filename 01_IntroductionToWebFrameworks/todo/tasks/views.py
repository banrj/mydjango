from django.http import HttpResponse

from django.views import View


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('<ul>'
                            '<li>Установить python</li>'
                            '<li>Установить django</li>'
                            '<li>Загуглить как это сделать через винду</li>'
                            '<li>Запустить сервер</li>'
                            '<li>Порадоваться результату</li>'
                            '</ul>')
