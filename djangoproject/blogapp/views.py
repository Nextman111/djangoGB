from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Article


def index(request):
    return HttpResponse("Blog main page")


def authors(request):
    query = Author.objects.all()
    return HttpResponse(query)


def articles(request):
    query = Article.objects.all()
    return HttpResponse(query)

# Create your views here.
