from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from app_users.forms import RegisterForm
from app_users.models import Profile, Product
from django.contrib.auth.mixins import PermissionRequiredMixin


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


class AccountTemplateView(TemplateView):
    template_name = 'app_users/account.html'


class MyLoginView(LoginView):
    template_name = 'app_users/login.html'


class MyLogoutView(LogoutView):
    pass
