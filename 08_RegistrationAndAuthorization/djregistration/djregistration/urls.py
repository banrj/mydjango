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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from app_users.views import (
    MyLoginView, MyLogoutView,
    MainListView, AccountTemplateView,
    Register, ProductDetailView,
    ProductCreateView, ProductUpdateView,
    OrderListView, OrderDetailView,
    OrdersExportDataView, ProfilesListView,
    ProfileDetailView, ProfileUpdateView,
    HelloView
)

from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path("orders/", OrderListView.as_view(), name="orders_list"),
    path("orders/<int:pk>", OrderDetailView.as_view(), name="order_detail"),
    path('account/', AccountTemplateView.as_view(), name='account'),
    path('register/', Register.as_view(), name='register'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product-update'),
    path('product/create', ProductCreateView.as_view(), name='creat-product'),
    path('orders/export', OrdersExportDataView.as_view(), name='order_export'),
    path('profiles', ProfilesListView.as_view(), name='profile_list'),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='profile_detail'),
    path('profile/<int:pk>/update', ProfileUpdateView.as_view(), name='profile_update'),
]

urlpatterns += i18n_patterns(
    path('hello/', HelloView.as_view()),
    path('', MainListView.as_view(), name='main'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
)
if settings.DEBUG:
    urlpatterns.extend(
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
