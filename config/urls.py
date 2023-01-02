from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    # user 관련 urls
    path("user/", include("dj_rest_auth.urls")),
    path("user/", include("dj_rest_auth.registration.urls")),
    path("user/", include("allauth.urls")),
    path("user/", include("user.urls")),
    path("project/", include("project.urls")),
    path("study/", include("study.urls")),
]
