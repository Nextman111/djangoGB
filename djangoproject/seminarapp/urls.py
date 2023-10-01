from django.urls import path
from .views import index, orelreshka, kosti, random_number


urlpatterns = [
    path('', index, name="index"),
    path('orelreshka/', orelreshka, name="orel ili reshka"),
    path('kosti/', kosti, name="kosti"),
    path('random_number', random_number, name="random number"),
]
