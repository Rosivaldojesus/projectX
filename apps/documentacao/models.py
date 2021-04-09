from django.db import models
from ..componentes.models import TiposDeSistemas


# Create your models here.

class Documentacao(models.Model):
    tituloDocumentacao = models.CharField(max_length=255, blank=True, null=True)
    textoDocumentacao = models.CharField(max_length=255, blank=True, null=True)
    sistemaDocumentacao = models.ForeignKey(TiposDeSistemas, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Documentação'

    def __str__(self):
        return "{}".format(self.tituloDocumentacao)

