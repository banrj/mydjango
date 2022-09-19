from django.urls import path
from . import views


urlpatterns = [
    path('advertisement/', views.Advertisement.as_view(), name='advertisement'),
    path('advertisement/accept_post/', views.Accept.as_view(), name='accept_post'),
    path('contacts/', views.Contacts.as_view(), name='contacts'),
    path('about/', views.About.as_view(), name='about'),
    path('', views.Face.as_view(), name='face')
]
