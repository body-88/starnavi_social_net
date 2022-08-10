from rest_framework import serializers

from posts.models.post import Post


class PostListSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    date_posted = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    link_to_post = serializers.HyperlinkedIdentityField(
        view_name="post-detail", lookup_field="pk"
    )

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "date_posted",
            "author",
            "link_to_post",
        )


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    date_posted = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Post
        fields = ("id", "title", "content", "date_posted", "author", "likes_count")


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "content",
        )
