from django.urls import path
from .views import index, \
    ClientShow, ClientAddEdit, ClientDelete, \
    ProductDelete, ProductAddEdit, ProductShow, OrderShow, OrderAddEdit, OrderDelete

urlpatterns = [
    path("", index, name='index'),

    path("clients/", ClientShow.as_view(), name='clients_page'),
    path("clients/edit/", ClientAddEdit.as_view(), name='client_edit'),
    path("clients/add/", ClientAddEdit.as_view(), name='client_add'),
    path("clients/del/<int:pk>", ClientDelete.as_view(), name='client_del'),

    path("products/", ProductShow.as_view(), name='products_page'),
    path("products/edit/", ProductAddEdit.as_view(), name='product_edit'),
    path("products/add/", ProductAddEdit.as_view(), name='product_add'),
    path("products/del/<int:pk>", ProductDelete.as_view(), name='product_del'),

    path("orders/", OrderShow.as_view(), name='orders_page'),
    path("orders/edit/", OrderAddEdit.as_view(), name='order_edit'),
    path("orders/add/", OrderAddEdit.as_view(), name='order_add'),
    path("orders/del/<int:pk>", OrderDelete.as_view(), name='order_del'),
]
