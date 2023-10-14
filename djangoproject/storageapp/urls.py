from django.urls import path
from .views import index, ClientShow, ClientAdd, ClientDelete

urlpatterns = [
    path("", index, name='index'),
    # path("clients/", client_show, name='Client page'),
    path("clients/", ClientShow.as_view(), name='client_page'),
    path("clients/add/", ClientAdd.as_view(), name='client_add'),
    path("clients/del/<int:pk>", ClientDelete.as_view(), name='client_del'),
]
