from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Administradora)
admin.site.register(Cidade)

admin.site.register(FabricanteCFTV)
admin.site.register(FabricanteSAI)
admin.site.register(FabricanteSCA)
admin.site.register(FabricanteSAP)
admin.site.register(FabricanteSDAI)

admin.site.register(TiposDeSistemas)
admin.site.register(ManuaisFabricante)
admin.site.register(ManuaisPreventiva)
admin.site.register(SenhasPadrao)