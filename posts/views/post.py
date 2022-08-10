from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from posts.models.post import Post
from posts.serializers.post import PostCreateSerializer
from posts.serializers.post import PostListSerializer
from posts.serializers.post import PostSerializer

# Create your views here.


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [AllowAny]


class PostRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]


class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = PostCreateSerializer
    permissions = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        author = request.user
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content")
        post = Post.objects.create(author=author, title=title, content=content)
        post.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
