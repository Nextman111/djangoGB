from django.urls import path
from .views import index, ClientShow, ClientAddEdit, ClientDelete

urlpatterns = [
    path("", index, name='index'),
    # path("clients/", client_show, name='Client page'),
    path("clients/", ClientShow.as_view(), name='client_page'),
    path("clients/edit/", ClientAddEdit.as_view(), name='client_edit'),
    path("clients/add/", ClientAddEdit.as_view(), name='client_add'),
    path("clients/del/<int:pk>", ClientDelete.as_view(), name='client_del'),
]
