from django.urls import path
from .views import *

app_name = 'article'


urlpatterns = [
    path('article-detail/<int:id>',
         article_detail, name='article_detail'),
    path('article-create/', article_create, name='article_create'),
    path('article-list/', article_list, name='article_list'),
    path('article-delete/<int:id>/', article_delete, name='article_delete'),
path('article-update/<int:id>/', article_update, name='article_update'),
]
