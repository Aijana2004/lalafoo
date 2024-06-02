from django.urls import path
from .views import ArticleListView, article_detail, article_new, article_edit

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>/', article_detail, name='article_detail'),
    path('article/new/', article_new, name='article_new'),
    path('article/<int:pk>/edit/', article_edit, name='article_edit'),
]
