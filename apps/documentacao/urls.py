from django.urls import path
from .views import Documentation, DocumentatioView, DocumentationEdit

urlpatterns = [
    path('', Documentation),
    path('documentationView/', DocumentatioView),
    path('editar/<int:pk>', DocumentationEdit.as_view(), name='update_documentation')


]
