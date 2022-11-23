from django.shortcuts import render
from django.views.generic import DetailView, ListView
from advertisements_app.models import Advertisement


class AdvertisementsListView(ListView):
    model = Advertisement
    template_name = 'advertisement_list.html'
    context_object_name = 'advertisement_list'


class AdvertisementDetailVIew(DetailView):
    model = Advertisement
