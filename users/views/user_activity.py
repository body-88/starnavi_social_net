from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users.models.users import User
from users.serializers.users import UserActivitySerializer


class UserActivityView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserActivitySerializer
    queryset = User.objects.all()
