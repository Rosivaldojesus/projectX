from django.db import models
#Importar o usuário
from django.contrib.auth.models import User
#Importat data
from django.utils import timezone


# Create your models here.

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categoria'

    def __str__(self):
        return "{}".format(self.nome_categoria)


class Post(models.Model):
    titulo_post = models.CharField(max_length=255)
    autor_post = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_post = models.DateTimeField(default=timezone.now)
    conteudo_post = models.TextField()
    excerto_post = models.TextField()
    categoria_post = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True, null=True)
    publicado_post = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Post'

    def __str__(self):
        return "{}".format(self.titulo_post)

class Comentario(models.Model):
    nome_comentario = models. CharField(max_length=150)
    email_comentario = models.EmailField()
    comentario = models.TextField()
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_comentario = models.DateTimeField(default=timezone.now)
    publicado_comentario = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Comentário'

    def __str__(self):
        return "{}".format(self.nome_comentario)

