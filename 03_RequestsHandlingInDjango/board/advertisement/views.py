from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .forms import ServiceForm, FaceForm


class ClassObj:
    count_get = 0
    count_post = 0


class Advertisement(View):
    def __init__(self):
        self.services = [
            'Электрик',
            'Сантехник',
            'Газовщик',
            'Штукатурщик'
        ]
        super(Advertisement, self).__init__()

    def get(self, request):
        print('get')
        ClassObj.count_get += 1
        user_form = ServiceForm()
        return render(request, "advertisements_app/advertisement_list.html", context={'services': self.services,
                                                                            'user_form': user_form,
                                                                            'count_get': ClassObj.count_get,
                                                                            'count_post': ClassObj.count_post})

    def post(self, request):
        print("post")
        ClassObj.count_post += 1
        return render(request, "advertisements_app/accept_post.html", {})


class Contacts(TemplateView):
    template_name = 'advertisements_app/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Contacts'
        context['address'] = 'Tokio, Green-street, 8-12'
        context['phone_number'] = '8-800-708-19-45'
        context['email'] = 'sales@company.com'
        return context


class About(TemplateView):
    template_name = 'advertisements_app/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'IT-Banrj'
        context['text'] = """
        Технологии инновационного развития дают беспрецедентную свободу выбора вариантов решений 
        для достижения оптимального результата. Мы уверены, что в современном мире информационные
        технологии являются одним из мощнейших инструментов развития бизнеса, 
        усиления его конкурентоспособности, улучшения условий и качества работы людей.
        """
        return context


class Face(View):

    def get(self, request):
        user_form = FaceForm()
        return render(request, 'advertisements_app/web_face.html', {'user_form': user_form})


class Accept(View):
    def get(self, request):
        return render(request, 'advertisements_app/accept_post.html', {})

    def post(self, request):
        ClassObj.count_post += 1
        return render(request, 'advertisements_app/accept_post.html', {})

