from django.contrib import admin
from app_users.models import Product


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['product_name']
    list_filter = ['created_by']
