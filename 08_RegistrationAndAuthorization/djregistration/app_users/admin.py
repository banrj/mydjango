from django.contrib import admin
from app_users.models import Product, Order, Profile


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['product_name']

    list_filter = ['created_by']


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ['user']


class ProductInline(admin.StackedInline):
    model = Order.products.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline
    ]
    list_display = "address", "promo_code", "created_at", "user_verbose"

    def get_queryset(self, request):
        return Order.objects.select_related("buyer").prefetch_related("products")

    @staticmethod
    def user_verbose(obj: Order) -> str:
        return obj.buyer.user.first_name or obj.buyer.user.username

