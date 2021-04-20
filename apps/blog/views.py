from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post, Comentario
from django.db.models import Q, Count, Case, When


# Create your views here.

class PostIndex(ListView):
    model = Post
    template_name = 'blog/indexx.html'
    context_object_name = 'posts'

    def get_queryset_data(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(publicado_post=True)
        qs = qs.annotate(
            numero_comentarios=Count(
                Case(
                    When(comentario__publicado_comentario=True, then=1)
                )
            )
        )
        qs1 = Comentario.objects.all()
        return qs, qs1





class PostBusca(PostIndex):
    pass

class Postcategoria(PostIndex):
    pass

class PostDetalhes(UpdateView):
    pass
    


