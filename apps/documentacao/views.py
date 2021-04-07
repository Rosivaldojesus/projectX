from django.shortcuts import render
from django.template.context_processors import request
from .models import Documentacao

# Create your views here.

def Documentation(request):
    cftv = Documentacao.objects.filter(sistemaDocumentacao=2)
    sai = Documentacao.objects.filter(sistemaDocumentacao=3)
    sap = Documentacao.objects.filter(sistemaDocumentacao=4)
    sca = Documentacao.objects.filter(sistemaDocumentacao=5)
    sdai =  Documentacao.objects.filter(sistemaDocumentacao=6)
    return render(request, 'documentacao/documentation.html', {'cftv':cftv,
                                                               'sai':sai,
                                                               'sap':sap,
                                                               'sca':sca,
                                                               'sdai':sdai,
                                                               })