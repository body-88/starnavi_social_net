from django.urls import path

from posts.views.analitics import LikeAnaliticsAPIView
from posts.views.like import LikeAPIView
from posts.views.post import PostCreateAPIView
from posts.views.post import PostListAPIView
from posts.views.post import PostRetrieveAPIView


urlpatterns = [
    path("", PostListAPIView.as_view()),
    path("create/", PostCreateAPIView.as_view()),
    path("analitics/", LikeAnaliticsAPIView.as_view()),
    path("<int:pk>/", PostRetrieveAPIView.as_view(), name="post-detail"),
    path("like/", LikeAPIView.as_view(), name="like-create"),
]
