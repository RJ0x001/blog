from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.shortcuts import render
from django.utils import dateformat
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .forms import UserRegisterForm, NewArticleForm
from .models import Article
from .filters import AuthorFilter


class CustomLoginRequiredMixin(LoginRequiredMixin):
    login_url = '/login/'


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm


class AllArticles(CustomLoginRequiredMixin, ListView):
    # filterset_class = AuthorFilter
    context_object_name = 'articles'
    paginate_by = 10
    # template_name = ...

    def get_queryset(self):
        author_filter = self.request.user
        return Article.objects.filter(author=author_filter).order_by('-created_time')


class ArticleDetails(CustomLoginRequiredMixin, DetailView):
    model = Article


class ArticleCreateView(CustomLoginRequiredMixin, CreateView):
    model = Article
    form_class = NewArticleForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




