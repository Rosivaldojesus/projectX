from django.db import models

# Create your models here.
#--------------------------------------------------------------------
#------------------    Administradora      --------------------------
#--------------------------------------------------------------------
class Administradora(models.Model):
    nome_administradora = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Administradora'

    def __str__(self):
        return self.nome_administradora
#--------------------------------------------------------------------
#------------------    Cidade      --------------------------
#--------------------------------------------------------------------
class Cidade(models.Model):
    cidade = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Cidade'

    def __str__(self):
        return self.cidade
#--------------------------------------------------------------------
#---------------    Fabricantes dos Sistemas     --------------------
#--------------------------------------------------------------------
class FabricanteCFTV(models.Model):
    nome_fabricante = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'FabricanteCFTV'

    def __str__(self):
        return self.nome_fabricante


class FabricanteSAI(models.Model):
    nome_fabricante = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'FabricanteSAI'

    def __str__(self):
        return self.nome_fabricante


class FabricanteSCA(models.Model):
    nome_fabricante = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'FabricanteSCA'

    def __str__(self):
        return self.nome_fabricante


class FabricanteSAP(models.Model):
    nome_fabricante = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'FabricanteSAP'

    def __str__(self):
        return self.nome_fabricante


class FabricanteSDAI(models.Model):
    nome_fabricante = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'FabricanteSDAI'

    def __str__(self):
        return self.nome_fabricante

#--------------------------------------------------------------------
#---------------    Tipos de  Sistemas     --------------------
#--------------------------------------------------------------------
class TiposDeSistemas(models.Model):
    tiposSistemas = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Tipos de Sistemas'

    def __str__(self):
        return "{}".format(self.tiposSistemas)

#--------------------------------------------------------------------
#------------------    Manuais Fabricantes    -----------------------
#--------------------------------------------------------------------
class ManuaisFabricante(models.Model):
    fabricanteNome = models.CharField(max_length=255, blank=True, null=True)
    fabricanteSistema = models.ForeignKey(TiposDeSistemas, on_delete=models.CASCADE)
    fabricanteLink = models.CharField(max_length=255, blank=True, null=True)
    fabricanteDescricao = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Manuais de Fabricanate'

    def __str__(self):
        return "{}".format(self.fabricanteNome)

#--------------------------------------------------------------------
#------------------    Manuais Preventiva    -----------------------
#--------------------------------------------------------------------
class ManuaisPreventiva(models.Model):
    preventivaEquipamento = models.CharField(max_length=255, blank=True, null=True)
    preventivaSistema = models.ForeignKey(TiposDeSistemas, on_delete=models.CASCADE)
    preventivaProcedimentos = models.CharField(max_length=255, blank=True, null=True)
    preventivaTempo = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Manuais de Preventivas'

    def __str__(self):
        return "{}".format(self.preventivaEquipamento)
#--------------------------------------------------------------------
#------------------    Manuais Preventiva    -----------------------
#--------------------------------------------------------------------
class SenhasPadrao(models.Model):
    senhaEquipamento = models.CharField(max_length=255, blank=True, null=True)
    senhaFabricante = models.ForeignKey(TiposDeSistemas, on_delete=models.CASCADE)
    senhaLogin = models.CharField(max_length=50, blank=True, null=True)
    senhaPassword = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = ' Senhas Padrão'

    def __str__(self):
        return "{}".format(self.senhaEquipamento)