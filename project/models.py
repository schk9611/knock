from django.db import models
from post.models import Post


class Position(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "position"


class ProjectInfo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    position = models.ManyToManyField(Position)

    class Meta:
        db_table = "project_info"
