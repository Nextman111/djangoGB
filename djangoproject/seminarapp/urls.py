from django.urls import path
from .views import index, kosti, random_number
from .views import orelreshka, orelreshka_stats
from .views import mainpage, aboutpage


urlpatterns = [
    path('', index, name="index"),
    path('orelreshka/', orelreshka, name="orel ili reshka"),
    path('orelreshka/stats/', orelreshka_stats, name="orel ili reshka stats"),
    path('kosti/', kosti, name="kosti"),
    path('random_number/', random_number, name="random number"),
    path('mainpage/', mainpage, name="main page"),
    path('aboutpage/', aboutpage, name="about page"),
]
