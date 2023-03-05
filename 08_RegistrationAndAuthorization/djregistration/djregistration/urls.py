"""djregistration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_users.views import (
    MyLoginView, MyLogoutView,
    MainListView, AccountTemplateView,
    Register, ProductDetailView,
    ProductCreateView, ProductUpdateView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('', MainListView.as_view(), name='main'),
    path('account/', AccountTemplateView.as_view(), name='account'),
    path('register/', Register.as_view(), name='register'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product-update'),
    path('product/create', ProductCreateView.as_view(), name='creat-product'),
]
