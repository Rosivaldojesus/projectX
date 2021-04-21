from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.PostIndex.as_view(), name='index'),
    path('categoria/<str:categoria>', views.Postcategoria.as_view(), name='post_categoria'),
    path('busca/', views.PostBusca.as_view(), name='post_busca'),
    path('post<int:pk>', views.PostDetalhes, name='post_detalhes'),

]


