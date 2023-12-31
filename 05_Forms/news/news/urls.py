"""news URL Configuration

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
from django.urls import path, include
from app_news.views import NewsFormView, NewsEditFormView, NewsWallListView, NewsDetailView, MyLoginView, MyLogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', NewsWallListView.as_view()),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('news', NewsFormView.as_view()),
    path('<int:news_id>/edit', NewsEditFormView.as_view()),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
]
