from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('clientes/', include('apps.clientes.urls')),
    path('forum/', include('apps.forum.urls')),
    path('documentacao/', include('apps.documentacao.urls')),
    path('blog/', include('apps.blog.urls')),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)