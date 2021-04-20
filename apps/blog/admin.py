from django.contrib import admin
from .models import Categoria, Post, Comentario



# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_categoria')
    list_display_links = ('id', 'nome_categoria')
admin.site.register(Categoria, CategoriaAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo_post','data_post', 'publicado_post')
    list_display_links = ('id', 'titulo_post','publicado_post')

admin.site.register(Post, PostAdmin)


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_comentario')

    list_display_links = ('id', 'nome_comentario')
admin.site.register(Comentario, ComentarioAdmin)