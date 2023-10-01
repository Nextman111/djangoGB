from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import logging

logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("Hello, World!")


def orelreshka(request):
    res = f"{'орел' if randint(0, 1) else 'решка'}"
    logger.info(res)
    return HttpResponse(res)


def kosti(request):
    res = f"{randint(1, 6)}"
    logger.info(res)
    return HttpResponse(res)


def random_number(request):
    res = f"{randint(0, 100)}"
    logger.info(res)
    return HttpResponse(res)


html = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <title>%title%</title>
</head>
<body>
    %content%
</body>
"""

def mainpage(request):
    title = "Главная страница Задания №8"
    content = "Эта страница с контентом главной страницы"

    res = html.replace("%title%", title)
    res = res.replace("%content%", content)

    logger.info(title)
    return HttpResponse(res)


def aboutpage(request):
    title = "Обо мне"
    content = """Эта страница должна была быть с информацией обо мне,
    но я не стал ей делиться:)"""

    res = html.replace("%title%", title)
    res = res.replace("%content%", content)

    logger.info(title)
    return HttpResponse(res)
