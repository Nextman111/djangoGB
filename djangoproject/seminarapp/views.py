from django.shortcuts import render
from django.http import HttpResponse
from random import randint

def index(request):
    return HttpResponse("Hello, World!")


def orelreshka(request):
    return HttpResponse(f"{'орел' if randint(0,1) else 'решка'}")


def kosti(request):
    return HttpResponse(f"{randint(1,6)}")


def random_number(request):
    return HttpResponse(f"{randint(0,100)}")
