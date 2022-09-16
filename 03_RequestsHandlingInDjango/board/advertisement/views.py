from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .forms import ServiceForm, FaceForm


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
        count = request.session.get('count')
        if not count:
            request.session['count'] = 1
        else:
            request.session['count'] += 1
        user_form = ServiceForm()
        return render(request, "advertisement/advertisement.html", context={'services': self.services,
                                                                            'user_form': user_form,
                                                                            'count': count})

    def post(self, request):
        request.session['count'] += 1
        user_form = ServiceForm(request.POST)

        if user_form.is_valid():
            self.take_argument(user_form)

    def take_argument(self, new_argument):
        self.services.append(new_argument)


class Contacts(TemplateView):
    template_name = 'advertisement/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Contacts'
        context['address'] = 'Tokio, Green-street, 8-12'
        context['phone_number'] = '8-800-708-19-45'
        context['email'] = 'sales@company.com'
        return context


class About(TemplateView):
    template_name = 'advertisement/about.html'

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
        return render(request, 'advertisement/web_face.html', {'user_form': user_form})


def accept(request, *args, **kwargs):
    return render(request, 'advertisement/accept_post.html', {})


