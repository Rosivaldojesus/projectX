from django.urls import path, include
from .views import ForumList, ForumCreate, ForumView, ForumListDetails

urlpatterns = [
    path('', ForumList, ),
    path('criar', ForumCreate.as_view(), name='create_forum'),

    #path('details/<int:id>', ForumPerguntaDetailView.as_view(), name='details_pergunta')
    path('teste/', ForumListDetails),
    path('testeview', ForumView)

]
