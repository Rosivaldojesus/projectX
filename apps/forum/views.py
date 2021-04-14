from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import PerguntaForum, RespostaForum


# Create your views here.
def Forum(request):
    pergunta = PerguntaForum.objects.all()
    return render(request, 'forum/forum.html', {'pergunta': pergunta})


class ForumPergunta(CreateView):
    model = PerguntaForum
    fields = ['titulo_pergunta','pergunta_forum']
    success_url = '/forum/'


def ForumPerguntaRespostas(request):
    pergunta = request.GET.get('id')
    if pergunta:
        pergunta = PerguntaForum.objects.get(id=pergunta)
    respostas = RespostaForum.objects.filter(resposta_pergunta=pergunta)
    return render(request, 'forum/perguntas-respostas.html', {'pergunta': pergunta,
                                                              'respostas': respostas,
                                                              })
