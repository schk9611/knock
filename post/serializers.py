from rest_framework import serializers
from .models import Post


class GenericPostSerializer(serializers.ModelSerializer):
    """post 모델 list, put, detail 요청에 사용"""

    author = serializers.ReadOnlyField(source="author.eamil")

    class Meta:
        model = Post
        fields = "__all__"


class PostCreateSerializer(serializers.ModelSerializer):
    """post 모델 create 요청에 사용"""

    author = serializers.ReadOnlyField(source="author.eamil")

    class Meta:
        model = Post
        exclude = ["is_active"]
