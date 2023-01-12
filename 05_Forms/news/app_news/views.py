from django.contrib.auth.views import LoginView, LogoutView
from django.forms import HiddenInput
from django.shortcuts import render
from app_news.forms import NewsModelForm, CommentsModelForm
from django.views import View
from app_news.models import News
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy


class NewsFormView(View):

    def get(self, request):
        news_form = NewsModelForm()
        return render(request, 'app_news/register.html', context={'news_form': news_form})

    def post(self, request):
        news_form = NewsModelForm(request.POST)

        if news_form.is_valid():
            News.objects.create(**news_form.cleaned_data)

            return HttpResponseRedirect('/')

        return render(request, 'app_news/register.html', context={'news_form': news_form})


class NewsEditFormView(View):

    def get(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = NewsModelForm(instance=news)
        return render(request, 'app_news/edit.html', context={'news_form': news_form, 'news_id': news_id})

    def post(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = NewsModelForm(request.POST, instance=news)

        if news_form.is_valid():
            news.save()

        return render(request, 'app_news/edit.html', context={'news_form': news_form, 'news_id': news_id})


class NewsWallListView(ListView):
    model = News
    template_name = 'app_news/news_list.html'
    context_object_name = 'all_news'


class NewsDetailView(FormMixin, DetailView):
    model = News
    form_class = CommentsModelForm

    success_msg = 'Комментарий успешно создан'
    
    def get_context_data(self, **kwargs):
        form = self.get_form()
        context = super(NewsDetailView, self).get_context_data()
        if context['view'].request.user.is_authenticated:
            form.fields['name'].widget = HiddenInput()
            context['form'] = form
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('news_detail', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            if request.user.is_authenticated:
                return self.form_valid(form, user=request.user, user_name=request.user.username)
            else:
                name = 'Anonim({})'.format(form.instance.name)
                return self.form_valid(form, user_name=name)
        return self.form_invalid(form)

    def form_valid(self, form, user=None, user_name=None):
        self.object = form.save(commit=False)
        self.object.user = user
        self.object.name = user_name
        self.object.news = self.get_object()
        self.object.save()
        return super().form_valid(form)


class MyLoginView(LoginView):
    template_name = 'app_news/login.html'
    next_page = '/'


class MyLogoutView(LogoutView):
    next_page = '/'
