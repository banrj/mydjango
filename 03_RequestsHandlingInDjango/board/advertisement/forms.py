from django import forms


class ServiceForm(forms.Form):
    your_service = forms.CharField(max_length=100)

    def __str__(self):
        return self.your_service


class FaceForm(forms.Form):

    search = forms.CharField(max_length=30)
    categories = forms.ChoiceField(widget=forms.RadioSelect, choices=[('Moscow', 'Moscow'), ('Sochi', 'Sochi'),
                                                                      ('Novosibirsk', 'Novosibirsk'), ('Ural', 'Ural')])
    regions = forms.ChoiceField(widget=forms.RadioSelect, choices=[('Поехать', 'Поехать'), ('Купить', 'Купить'),
                                                                   ('Полететь', 'Полететь'),
                                                                   ('Посмотерть', 'Посмотерть'),
                                                                   ('Забрать', 'Забрать')])
