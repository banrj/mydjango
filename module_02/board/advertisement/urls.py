from django.urls import path
from .import views

urlpatterns = [
    path('advertisement/', views.advertisement_detail, name='advertisement_list'),
    path('pythonbasic/', views.python_basic, name='python_basic'),
    path('pythonadvanced/', views.python_advanced, name='python_advanced'),
    path('pythondjango/', views.python_django, name='python_django'),
    path('verstkabasic/', views.verstka_basic, name='verstka_basic'),
    path('verstkaadvanced/', views.verstka_advanced, name='verstka_advanced/'),
]


