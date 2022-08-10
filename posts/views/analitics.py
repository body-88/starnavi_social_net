from itertools import groupby

from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from posts.filters import LikeAnaliticsFilter
from posts.models.like import Like


class LikeAnaliticsAPIView(generics.GenericAPIView):
    queryset = Like.objects.all()
    filterset_class = LikeAnaliticsFilter
    permission_classes = [IsAuthenticated]

    def grouper(self, item):
        return item.date_created.date()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        filtered_queryset = self.filter_queryset(queryset)
        ordered_queryset = filtered_queryset.order_by("-date_created")
        grouped_likes = groupby(ordered_queryset, key=self.grouper)
        analytics = []
        for date, like in grouped_likes:
            analytics.append({"date": date, "likes": len(list(like))})
        return Response(analytics, status.HTTP_200_OK)
