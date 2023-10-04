import logging

from django.db import models
from django.utils import timezone


# Модель для орла и решки
class OrelReshka(models.Model):
    roll_result = models.BooleanField(verbose_name="Результат")
    roll_time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'{self.roll_time} - {self.roll_result}'

    @staticmethod
    def get_rolls(n):
        query = OrelReshka.objects.all()[:n]
        return query
