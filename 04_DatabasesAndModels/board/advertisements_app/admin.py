from django.contrib import admin
from advertisements_app.models import Advertisement, AdvertisementCategories, Host

# Register your models here.


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvertisementCategories)
class AdvertisementCategories(admin.ModelAdmin):
    pass


@admin.register(Host)
class Host(admin.ModelAdmin):
    pass
