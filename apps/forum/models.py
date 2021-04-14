from django.db import models


# Create your models here.


class PerguntaForum(models.Model):
    titulo_pergunta = models.CharField(max_length=255, blank=True, null=True)
    pergunta_forum = models.CharField(max_length=251, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Pergunta Fórum'

    def __str__(self):
        return "{}".format(self.titulo_pergunta)


class RespostaForum(models.Model):
    resposta = models.CharField(max_length=253, blank=True, null=True)
    resposta_pergunta = models.ForeignKey(PerguntaForum, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Resposta Fórum'

    def __str__(self):
        return "{}".format(self.resposta)

class ComentariosRespostaForum(models.Model):
    comentario = models.CharField(max_length=255, blank=True, null=True)
    respostaForum = models.ForeignKey(RespostaForum, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Comentário Resposta'

    def __str__(self):
        return "{}".format(self.comentario)


