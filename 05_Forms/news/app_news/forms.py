from django import forms
from app_news.models import News, Comments


class NewsModelForm(forms.ModelForm):

    class Meta:
        model = News
        fields = '__all__'


class CommentsModelForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('name', 'text')
