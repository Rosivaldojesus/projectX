from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import PerguntaForum

# Create your views here.
class ForumList(ListView):
    model = PerguntaForum

class ForumCreate(CreateView):
    model = PerguntaForum
    fields = ['titulo_pergunta','pergunta_forum']
    success_url = '/forum/'
