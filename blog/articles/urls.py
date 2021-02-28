from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('articles/', views.AllArticles.as_view(), name='articles_list'),
    path('articles/<int:pk>', views.ArticleDetails.as_view(), name='article_detail'),
    path('articles/new/', views.ArticleCreateView.as_view(), name='article_create'),
]
