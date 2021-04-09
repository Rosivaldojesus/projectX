from django.shortcuts import render
from .models import Documentacao

from django.views.generic.edit import UpdateView


# Create your views here.

def Documentation(request):
    cftv = Documentacao.objects.filter(sistemaDocumentacao=2)
    sai = Documentacao.objects.filter(sistemaDocumentacao=3)
    sap = Documentacao.objects.filter(sistemaDocumentacao=4)
    sca = Documentacao.objects.filter(sistemaDocumentacao=5)
    sdai = Documentacao.objects.filter(sistemaDocumentacao=6)
    return render(request,
                  'documentacao/documentation.html',
                  {'cftv': cftv,
                   'sai': sai,
                   'sap': sap,
                   'sca': sca,
                   'sdai': sdai
                   })


def DocumentatioView(request):
    doc = request.GET.get('id')
    if doc:
        doc = Documentacao.objects.get(id=doc)
    return render(request,
                  'documentacao/documentationView.html',
                  {'doc': doc
                   })


class DocumentationEdit(UpdateView):
    model = Documentacao
    fields = ['tituloDocumentacao', 'textoDocumentacao']
    success_url = "/documentacao/"
