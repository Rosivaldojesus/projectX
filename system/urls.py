from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('clientes/', include('apps.clientes.urls')),
    path('forum/', include('apps.forum.urls')),
    path('documentacao/', include('apps.documentacao.urls')),

]
