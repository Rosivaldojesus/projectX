from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import PerguntaForum, RespostaForum


# Create your views here.


def ForumList(request):
    pergunta = PerguntaForum.objects.all()
    respostasPerguntas = RespostaForum.objects.filter().count()
    return render(request, 'forum/perguntaforum_list.html', {'pergunta':pergunta,
                                                              'respostasPerguntas':respostasPerguntas

                                                              })


def ForumListDetails(request):
    pergunta = request.GET.get('id')
    if pergunta:
        pergunta = PerguntaForum.objects.get(id=pergunta)
    resposta = RespostaForum.objects.filter(resposta_pergunta=pergunta)
    respostasPerguntas = RespostaForum.objects.filter(resposta_pergunta=pergunta).count()
    return render(request, 'forum/perguntaforum_detail.html',{'resposta':resposta,
                                                              'pergunta':pergunta,
                                                              'respostasPerguntas':respostasPerguntas,

                                                              })



def ForumView(request):
    pergunta = request.GET.get('id')
    dados = {}
    if pergunta:
        dados['pergunta'] = RespostaForum.objects.get(id=pergunta)
    return render(request, 'forum/testeview.html', dados)



class ForumCreate(CreateView):
    model = PerguntaForum
    fields = ['titulo_pergunta','pergunta_forum']
    success_url = '/forum/'
