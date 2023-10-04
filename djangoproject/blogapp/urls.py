from django.urls import path
from .views import index, authors, articles


urlpatterns = [
    path('', index, name="index"),
    path('authors/', authors, name="authors"),
    path('articles/', articles, name="articles"),
]
