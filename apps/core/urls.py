from django.urls import path, include
from .views import home, Senha, Manuais

urlpatterns = [
    path('', home),
    path('senhas-padrao/', Senha),
    path('manuais/', Manuais)

]
