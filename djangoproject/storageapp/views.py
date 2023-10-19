import logging

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, FormView

from .forms import ClientForm, ProductForm, OrderForm
from .models import Client, Product, Order

logger = logging.getLogger(__name__)


def index(request):
    context = {
        'title': 'Main page storage',
        'content': "Наполнение магазина",
    }
    return render(request, 'storageapp/index.html', context)


class ItemsShow(TemplateView):
    template_name = "storageapp/items.html"
    title = "Item list"
    entity = None
    del_page = ""
    edit_page = ""
    add_page = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title

        query = self.entity.objects.all()
        context['content'] = query
        context['edit_page'] = self.edit_page
        context['del_page'] = self.del_page
        context['add_page'] = self.add_page

        return context


class ItemDelete(View):
    entity = None
    redirect_page = "."

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        query = self.entity.objects.get(pk=pk)
        if query:
            query.delete()
        return redirect(self.redirect_page)


class ItemAddEdit(FormView):
    template_name = "storageapp/item_form.html"
    form_class = None
    success_url = '../'
    entity = None
    title = ""

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)

        if not self.request.GET.get('pk') is None:
            query = self.entity.objects.filter(pk=self.request.GET.get('pk')).first()
            form = self.form_class(initial=query.as_dict())
            title = f"Edit {self.title} with id: {query.pk}"
        else:
            title = f"Add new {self.title}"
            form = self.form_class()

        return {'form': form, 'title': title}

    def form_valid(self, form):
        query = self.entity(
            pk=self.request.GET.get('pk'),
            **form.cleaned_data
        )
        query.save()
        logger.info(f"Add new {self.title} {query}")

        return super().form_valid(form)


class ClientAddEdit(ItemAddEdit):
    title = "Client"
    entity = Client
    form_class = ClientForm


class ClientShow(ItemsShow):
    title = "Список клиентов"
    entity = Client
    del_page = "client_del"
    edit_page = "client_edit"
    add_page = "client_add"


class ClientDelete(ItemDelete):
    title = "Список клиентов"
    entity = Client
    redirect_page = 'clients_page'


class ProductAddEdit(ItemAddEdit):
    title = "Product"
    entity = Product
    form_class = ProductForm


class ProductShow(ItemsShow):
    title = "Список клиентов"
    entity = Product
    del_page = "product_del"
    edit_page = "product_edit"
    add_page = "product_add"


class ProductDelete(ItemDelete):
    title = "Удаление продукта"
    entity = Product
    redirect_page = 'products_page'


class OrderAddEdit(ItemAddEdit):
    title = "Заказ"
    entity = Order
    form_class = OrderForm

    def form_valid(self, form):
        client = form.cleaned_data.get('client')
        costing = form.cleaned_data.get('costing')

        products = form.cleaned_data.get('product')

        instance = Order.objects.create(
            client=client,
            costing=costing,
        )

        instance.save()
        instance.product.add(*products)
        instance.save()

        # products = form.cleaned_data.get('product')

        # print(instance)

        # print(form.cleaned_data['product'])
        # products = []
        # for item in form.cleaned_data['product']:
        #     products.append(Product.objects.filter(pk=item.pk))
        #
        # print("asdasdasdasdasdadasdasda")
        #
        # print(products)
        #
        #
        # form.cleaned_data['product'] = products
        # form.save()
        # order.product.set(products)

        # order.save()
        # logger.info(f"Add new {self.title} Order")

        # return super().form_valid(form)
        return redirect(self.success_url)


class OrderShow(ItemsShow):
    template_name = "storageapp/orders.html"
    title = "Список заказов"
    entity = Order
    del_page = "order_del"
    edit_page = "order_edit"
    add_page = "order_add"


class OrderDelete(ItemDelete):
    title = "Удаление заказа"
    entity = Order
    redirect_page = 'orders_page'
