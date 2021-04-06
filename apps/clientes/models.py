from django.db import models
from django.urls import reverse
from ..componentes.models import *

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    adm = models.ForeignKey(Administradora, on_delete=models.CASCADE, blank=True, null=True)
    fabricanteCFTV = models.ForeignKey(FabricanteCFTV, on_delete=models.CASCADE, blank=True, null=True)
    fabricanteSAI = models.ForeignKey(FabricanteSAI, on_delete=models.CASCADE, blank=True, null=True)
    fabricanteSCA = models.ForeignKey(FabricanteSCA, on_delete=models.CASCADE, blank=True, null=True)
    fabricanteSAP = models.ForeignKey(FabricanteSAP, on_delete=models.CASCADE, blank=True, null=True)
    fabricanteSDAI = models.ForeignKey(FabricanteSDAI, on_delete=models.CASCADE, blank=True, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, blank=True, null=True)


    def get_absolute_url(self):
        return reverse('list_cliente')

    def __str__(self):
        return self.nome


