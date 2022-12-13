from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("post/", include("post.urls")),
    path("user/", include("user.urls")),
    path("project/", include("project.urls")),
    path("study/", include("study.urls")),
]
