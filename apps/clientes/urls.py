from django.urls import path, include
from .views import ClienteCreate, ClienteEdit,ClienteList, ClienteDelete

from .views import ClienteDetailView

urlpatterns = [
    path('', ClienteList.as_view(), name='list_cliente'),
    path('criar', ClienteCreate.as_view(), name='create_cliente'),
    path('editar/<int:pk>/', ClienteEdit.as_view(), name='update_cliente'),
    path('delete/<int:pk>/', ClienteDelete.as_view(), name='delete_cliente'),

    path('details/<int:pk>', ClienteDetailView.as_view(), name='details_cliente')

]
