from django.urls import path, include
from .views import Documentation

urlpatterns = [
    path('', Documentation),


]
