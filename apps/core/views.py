from django.shortcuts import render
from ..componentes.models import SenhasPadrao, ManuaisFabricante


# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def Senha(request):
    senha = SenhasPadrao.objects.all()
    return render(request, 'core/senhas-padrao.html', {'senha': senha})

def Manuais(request):
    manual = ManuaisFabricante.objects.all()
    return render(request, 'core/manuais.html', {'manual': manual})

