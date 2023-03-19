from django.shortcuts import render
from django.http import JsonResponse
from django.views import View


class FooBarView(View):
    def get(self, request):
        return JsonResponse({'foo': "bar", 'spam': 'eggs'})
