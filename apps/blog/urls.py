from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.PostIndex.as_view(), name='index'),
    path('categoria/<str:categoria>', views.Postcategoria.as_view(), name='post_categoria'),
    path('busca/', views.PostBusca.as_view(), name='post_busca'),
    path('post<int:pk>', views.PostDetalhes, name='post_detalhes'),
    path('summernote/', include('django_summernote.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

