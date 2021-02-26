from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.utils import dateformat

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .forms import UserRegisterForm
from .models import Article


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm


class AllArticles(ListView):
    queryset = Article.objects.all()
    context_object_name = 'articles'
    # paginate_by = 2


class ArticleDetails(DetailView):
    model = Article





