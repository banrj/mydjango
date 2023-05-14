from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_users.models import Profile
from django.forms import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class ProfileForm(forms.Form):
    class Meta:
        model = Profile
        fields = 'avatar'
