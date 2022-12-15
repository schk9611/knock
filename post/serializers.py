from rest_framework import serializers
from .models import Post

class GenericPostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.eamil')

    class Meta:
        model = Post
        fields = "__all__"
        