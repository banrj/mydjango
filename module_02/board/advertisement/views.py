from django.shortcuts import render
from django.http import HttpResponse


def advertisement_detail(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_list.html', {})


def python_basic(request, *args, **kwargs):
    return render(request, 'advertisement/python_basic_page.html', {})


def python_django(request, *args, **kwargs):
    return render(request, 'advertisement/python_django_page.html', {})


def python_advanced(request, *args, **kwargs):
    return render(request, 'advertisement/python_advanced_page.html', {})


def verstka_basic(request, *args, **kwargs):
    return render(request, 'advertisement/verstka_basic_page.html', {})


def verstka_advanced(request, *args, **kwargs):
    return render(request, 'advertisement/verstka_advanced_page.html', {})

