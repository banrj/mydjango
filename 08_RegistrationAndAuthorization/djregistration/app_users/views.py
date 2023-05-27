from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from app_users.forms import RegisterForm, ProfileForm
from app_users.models import Profile, Product, Order
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.utils.translation import gettext_lazy as _


class Register(CreateView):
    template_name = 'app_users/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('account')

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password2')
        user = authenticate(
            self.request, username=username, password=password
        )

        login(self.request, user)

        return response


class MainListView(ListView):
    template_name = 'app_users/main.html'
    model = Product
    context_object_name = 'products'


class OrderListView(ListView):
    queryset = (
        Order.objects.select_related("buyer").prefetch_related("products")
    )
    context_object_name = 'orders'


class OrderDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ['app_users.view_order']
    queryset = (
        Order.objects.select_related("buyer").prefetch_related("products")
    )
    context_object_name = 'order'


class ProductDetailView(DetailView):
    template_name = 'app_users/product-detail.html'
    model = Product
    context_object_name = 'product'


class ProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ['app_users.add_product']
    template_name = 'app_users/add-product.html'
    model = Product
    fields = 'product_name', 'price', 'options'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.instance.created_by = self.request.user.profile
        response = super().form_valid(form)
        form.save()
        return response


class ProductUpdateView(PermissionRequiredMixin, UpdateView):

    permission_required = ['app_users.change_product']
    template_name = 'app_users/update-product.html'
    model = Product
    fields = 'product_name', 'price', 'options'

    def get_success_url(self):
        return reverse('product-detail', kwargs={'pk': self.object.pk},)

    def has_permission(self):
        has_perms = super().get_permission_required()
        if (self.request.user.profile == self.get_object().created_by
                or self.request.user.is_superuser):
            return self.request.user.has_perms(has_perms)
        return False


class AccountTemplateView(TemplateView):
    template_name = 'app_users/account.html'


class MyLoginView(LoginView):
    template_name = 'app_users/login.html'


class MyLogoutView(LogoutView):
    pass


class OrdersExportDataView(PermissionRequiredMixin, View):
    permission_required = 'is_staff'
    @staticmethod
    def get(request: HttpRequest) -> JsonResponse:
        orders = Order.objects.order_by('pk').all()
        orders_data = [
            {
                "pk": order.pk,
                "address": order.address,
                "promo_code": order.promo_code,
                'buyer': order.buyer.user.id,
                'products': [product.id for product in order.products.all()]

            }
            for order in orders
        ]
        return JsonResponse({"orders": orders_data})


class ProfilesListView(ListView):
    queryset = (
        Profile.objects.all().select_related('user')
    )
    context_object_name = 'profiles'
    template_name = 'app_users/profile_list.html'


class ProfileDetailView(DetailView):
    queryset = (
        Profile.objects.all().select_related('user')
    )
    context_object_name = 'profile'


class ProfileUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = []
    template_name = 'app_users/profile_update.html'
    model = Profile
    fields = ('avatar', )

    def get_success_url(self):
        return reverse('profile_detail', kwargs={'pk': self.object.pk},)

    def has_permission(self):
        has_perm = super().has_permission()

        if not has_perm:
            return has_perm

        return self.request.user.profile == self.get_object() or self.request.user.is_superuser


class HelloView(View):
    translate_message = _("Привет, мир!")

    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse(self.translate_message)
