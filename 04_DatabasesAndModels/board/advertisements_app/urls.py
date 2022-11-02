from django.urls import path
from . import views

urlpatterns = [
    path('advertisements/', views.AdvertisementsListView.as_view(), name='advertisements'),
    path('advertisements/<int:pk>', views.AdvertisementDetailVIew.as_view(), name='advertisement-detaeil'),
]
