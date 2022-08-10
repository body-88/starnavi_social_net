from rest_framework import serializers

from posts.models.like import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ("post",)
