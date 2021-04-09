from django.urls import reverse
from ..componentes.models import *


# Create your models here.
# Models dos clientes, onde consta as informações relevantes de
#cada cliente
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


#Models para os equipamentos relacionados nos respectivos clientes
class EquipamentosCliente(models.Model):
    equipamentoNome = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    equipamentoLogin = models.CharField(max_length=100, blank=True, null=True)
    equipamentoPassword = models.CharField(max_length=100, blank=True, null=True)
    equipamentoLocalizacao = models.CharField(max_length=255, blank=True, null=True)
    equipamentoTexto = models.CharField(max_length=255, blank=True, null=True)
    equipamentoSistema = models.ForeignKey(TiposDeSistemas, on_delete=models.CASCADE)
    equipamentoCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Equipamentos cliente'

    def __str__(self):
        return "{}".format(self.equipamentoNome)
