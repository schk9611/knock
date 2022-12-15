from django.db import models
from django.conf import settings


class DevStack(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="", blank=True)

    class Meta:
        db_table = "dev_stack"

    def __str__(self):
        return self.name

class Post(models.Model):
    POST_TYPE = [
        ("PR", "Project"),
        ("ST", "Study"),
    ]
    MEET_TYPE = [
        ("ON", "Online"),
        ("OF", "Offline"),
    ]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    crew = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="crews")
    dev_tag = models.ManyToManyField(DevStack)
    post_type = models.CharField(max_length=2, choices=POST_TYPE)
    meet_type = models.CharField(max_length=2, choices=MEET_TYPE)
    location_info = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="", blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "post"
