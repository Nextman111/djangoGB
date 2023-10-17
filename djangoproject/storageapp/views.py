import logging

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, FormView
from django.views.generic.edit import DeletionMixin

from .forms import ClientForm
from .models import Client

logger = logging.getLogger(__name__)


def index(request):
    context = {
        'title': 'Main page storage',
        'content': "Наполнение магазина",
    }
    return render(request, 'storageapp/index.html', context)


class ClientShow(TemplateView):
    template_name = "storageapp/clients.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Список клиентов"

        clients = Client.objects.all()
        context['content'] = clients

        return context


class ClientDelete(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.get(pk=pk)
        if client:
            client.delete()
        return redirect('client_page')


class ClientAddEdit(FormView):
    template_name = "storageapp/client.html"
    form_class = ClientForm
    success_url = '../'

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)

        if not self.request.GET.get('pk') is None:
            client = Client.objects.filter(pk=self.request.GET.get('pk')).first()
            form = ClientForm(initial=client.as_dict())
            title = f"Edit Client with id: {client.pk}"
        else:
            title = "Add new Client"
            form = ClientForm()

        return {'form': form, 'title': title}

    def form_valid(self, form):
        client = Client(
            pk=self.request.GET.get('pk'),
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            phone=form.cleaned_data['phone'],
            adress=form.cleaned_data['adress'],
            date_reg=form.cleaned_data['date_reg'],
        )
        client.save()
        logger.info(f"Add new Client {client.name}")

        return super().form_valid(form)
