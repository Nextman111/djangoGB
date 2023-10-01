from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import logging

logger = logging.getLogger(__name__)

def index(request):
    return HttpResponse("Hello, World!")


def orelreshka(request):
    res = f"{'орел' if randint(0,1) else 'решка'}"
    logger.info(res)
    return HttpResponse(res)


def kosti(request):
    return HttpResponse(f"{randint(1,6)}")


def random_number(request):
    return HttpResponse(f"{randint(0,100)}")
