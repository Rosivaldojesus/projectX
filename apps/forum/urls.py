from django.urls import path, include
from .views import ForumList, ForumCreate

urlpatterns = [
    path('', ForumList.as_view(), name='list_forum'),
    path('criar', ForumCreate.as_view(), name='create_forum'),


]
