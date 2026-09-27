from django.urls import path
from articles.views import article_create, article_detail

urlpatterns = [
    path('articles/', article_create),
    path('articles/<int:pk>', article_detail)
]