from django.urls import path
from . import views


urlpatterns = [
    path('advertisements_app/', views.Advertisement.as_view(), name='advertisements_app'),
    path('advertisements_app/accept_post/', views.Accept.as_view(), name='accept_post'),
    path('contacts/', views.Contacts.as_view(), name='contacts'),
    path('about/', views.About.as_view(), name='about'),
    path('', views.Face.as_view(), name='face')
]
