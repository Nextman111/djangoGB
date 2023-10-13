from django.urls import path
from .views import index, ClientShow, ClientAdd

urlpatterns = [
    path("", index, name='index'),
    # path("clients/", client_show, name='Client page'),
    path("clients/", ClientShow.as_view(), name='Client page'),
    path("clients/add", ClientAdd.as_view(), name='Client add'),
]
