from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Cliente, EquipamentosCliente


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


def Equipamentos(request):
    equipamento = request.GET.get('id')
    dados = {}
    if equipamento:
        dados['equipamento'] = EquipamentosCliente.objects.filter(
            equipamentoCliente=equipamento
        )
    return render(request, 'equipamentos.html', dados)



class EquipamentosDetalhes(DetailView):
    model = EquipamentosCliente


