
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cliente
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.
class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome',
              'adm',
              'fabricanteCFTV',
              'fabricanteSAI',
              'fabricanteSCA',
              'fabricanteSAP',
              'fabricanteSDAI',
              'cidade']
    success_url = '/clientes/'


class ClienteList(ListView):
    model = Cliente

class ClienteDetailView(DetailView):
    model = Cliente


class ClienteEdit(UpdateView):
    model = Cliente
    fields = ['nome',
              'adm',
              'fabricanteCFTV',
              'fabricanteSAI',
              'fabricanteSCA',
              'fabricanteSAP',
              'fabricanteSDAI',
              'cidade']

class ClienteDelete(DeleteView):
    model = Cliente

    success_url = reverse_lazy('list_cliente')



