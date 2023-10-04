import random

from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import logging

from django.utils import timezone

from .models import OrelReshka

logger = logging.getLogger(__name__)

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


def index(request):
    return HttpResponse("Hello, World!")


def orelreshka(request):
    roll = random.choice([True, False])
    obj = OrelReshka(roll_result=roll, roll_time=timezone.now())
    obj.save()

    res = f"{'орел' if roll else 'решка'}"
    logger.info(res)
    # OrelReshka.get_rolls(4)
    return HttpResponse(f'Время броска {obj.roll_time} - результат {obj.roll_result}')


def orelreshka_stats(request):
    n = str(request.GET.get("n", "1"))
    if n.isnumeric():
        res = OrelReshka.get_rolls(int(n))
        stats = 0

        for i in res:
            if i.roll_result:
                stats += 1

        content = f"<p>Статистика по последним {n} записям:</p>"
        content += f"<p>Орел: {stats}, Решка: {int(n)-stats}</p>"
        content += "".join([f"<p>{i}</p>" for i in list(res)])

        page = html.replace("%title%", f"Статистика по {n} броскам")

        page = page.replace("%content%", content)
    else:
        page = html.replace("%title%", f"Ошибка аргумента")
        page = page.replace("%content%", "Неверный аргумент")

    return HttpResponse(page)


def kosti(request):
    res = f"{randint(1, 6)}"
    logger.info(res)
    return HttpResponse(res)


def random_number(request):
    res = f"{randint(0, 100)}"
    logger.info(res)
    return HttpResponse(res)


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
