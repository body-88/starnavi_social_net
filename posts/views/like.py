from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models.like import Like
from posts.serializers.like import LikeSerializer


class LikeAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LikeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        post_id = serializer.validated_data.get("post")

        user = request.user
        if Like.objects.filter(post=post_id, user=user).exists():
            Like.objects.filter(post=post_id, user=user).delete()
            return Response(
                {"message": "Post successfully unliked"}, status.HTTP_200_OK
            )
        else:
            Like.objects.create(post=post_id, user=user)
            return Response({"message": "Post successfully liked"}, status.HTTP_200_OK)
