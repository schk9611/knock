from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from .models import Post
from .serializers import GenericPostSerializer, PostCreateSerializer


class GenericPostModelViewSet(ModelViewSet):
    """
    localhost/post/
    localhost/post/<int:pk>/
    """

    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return GenericPostSerializer
        if self.action == "create":
            return PostCreateSerializer
        return GenericPostSerializer

    def create(self, request, *args, **kwargs):
        """ModelViewSet create 매서드"""
        serializer = self.get_serializer(data=request.data)
        # create시 사용하는 serializer
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"data": serializer.data}, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        """
        해당 유저정보를 form, json을 통하지 않고 request 통해 저장
        """
        serializer.save(author=self.request.user)
