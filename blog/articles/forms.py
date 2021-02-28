from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Article


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', ]


class NewArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'text',
        ]
