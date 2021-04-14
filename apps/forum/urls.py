from django.urls import path

from .views import Forum, ForumPergunta, ForumPerguntaRespostas




urlpatterns = [

    path('', Forum),
    path('criar', ForumPergunta.as_view(), name='create_pergunta'),
    path('perguntas-respostas/', ForumPerguntaRespostas),








]
