import logging

from timeit import default_timer

from django.core import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound, Http404
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.core.cache import cache
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .forms import ProductForm
from .models import Product, Order, ProductImage


log = logging.getLogger(__name__)


class ShopIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        products = [
            ('Laptop', 1999),
            ('Desktop', 2999),
            ('Smartphone', 999),
        ]
        context = {
            "time_running": default_timer(),
            "products": products,
        }
        log.debug("Products for shop index %s", products)
        log.info('Info about products')
        print('shop index context', context)
        return render(request, 'shopapp/shop-index.html', context=context)


class ProductDetailsView(DetailView):
    template_name = "shopapp/products-details.html"
    queryset = Product.objects.prefetch_related("images")
    context_object_name = "product"


class ProductsListView(ListView):
    template_name = "shopapp/products-list.html"
    context_object_name = "products"
    queryset = Product.objects.filter(archived=False)


class ProductCreateView(CreateView):
    model = Product
    fields = "name", "price", "description", "discount", "preview"
    success_url = reverse_lazy("shopapp:products_list")


class ProductUpdateView(UpdateView):
    model = Product
    # fields = "name", "price", "description", "discount", "preview"
    template_name_suffix = "_update_form"
    form_class = ProductForm

    def get_success_url(self):
        return reverse(
            "shopapp:product_details",
            kwargs={"pk": self.object.pk},
        )

    def form_valid(self, form):
        response = super().form_valid(form)
        for image in form.files.getlist("images"):
            ProductImage.objects.create(
                product=self.object,
                image=image,
            )

        return response


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("shopapp:products_list")

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class OrdersListView(LoginRequiredMixin, ListView):
    queryset = (
        Order.objects
        .select_related("user")
        .prefetch_related("products")
    )


class OrderDetailView(PermissionRequiredMixin, DetailView):
    permission_required = "shopapp.view_order"
    queryset = (
        Order.objects
        .select_related("user")
        .prefetch_related("products")
    )


class ProductsDataExportView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        cache_key = "products_data_export"
        products_data = cache.get(cache_key)
        if not products_data:

            products = Product.objects.order_by('pk').all()
            products_data = [
                {
                    "pk": product.pk,
                    "name": product.name,
                    "price": product.price,
                    "archived": product.archived,
                }
                for product in products
            ]
            cache.set(cache_key, products_data, 30)
        return JsonResponse({"products": products_data})


class UserOrdersListView(LoginRequiredMixin, ListView):
    template_name = 'shopapp/user-order-list.html'

    def get_queryset(self):
        queryset = (
            Order.objects
            .select_related("user")
            .prefetch_related("products").filter(user=self.request.user)
        )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["orders"] = self.get_queryset()
        context['user'] = self.request.user
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise Http404()
        return super().dispatch(request, *args, **kwargs)


class UserOrdersExportView(View):

    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        cache_key = 'user_orders_export_{}'.format(pk)
        try:
            user = User.objects.get(id=pk)
        except ObjectDoesNotExist:
            raise Http404

        orders_data = cache.get(cache_key)
        print(orders_data)
        if not orders_data or orders_data == []:
            orders = (Order.objects
                      .select_related("user").filter(user=user)
                      .prefetch_related("products"))
            raw_data = serializers.serialize('json', orders)
            cache.set(cache_key, raw_data, 10)
            orders_data = cache.get(cache_key)
        return JsonResponse({"user": user.username,
                             "orders": orders_data})
