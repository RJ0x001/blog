import django_filters

from .models import Article


class AuthorFilter(django_filters.FilterSet):

    class Meta:
        model = Article
        fields = ['author', ]
