from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .forms import UserRegisterForm, NewArticleForm
from .models import Article


class CustomLoginRequiredMixin(LoginRequiredMixin):
    login_url = '/login/'


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm


class AllArticles(CustomLoginRequiredMixin, ListView):
    context_object_name = 'articles'
    paginate_by = 5

    def get_queryset(self):
        author_filter = self.request.user
        return Article.objects.filter(author=author_filter).order_by('-created_time')


class ArticleDetailView(CustomLoginRequiredMixin, DetailView):
    model = Article

    fields = ['title', 'text']


class ArticleCreateView(CustomLoginRequiredMixin, CreateView):
    model = Article
    form_class = NewArticleForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    success_url = ''

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False
