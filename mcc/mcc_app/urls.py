from django.urls import path
from .views import create_article, article_list

urlpatterns = [
    path('', article_list, name='article_list'),
    path('new/', create_article, name='create_article'),
]
