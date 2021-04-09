from django.urls import path
from .views import ForumList, ForumCreate, ForumView, ForumListDetails

urlpatterns = [
    path('', ForumList, ),
    path('criar', ForumCreate.as_view(), name='create_forum'),
    path('teste/', ForumListDetails),
    path('testeview', ForumView)
]
