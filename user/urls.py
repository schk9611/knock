from rest_framework import routers
from django.urls import path, include

from .views import UserViewSet, google_login, google_callback, GoogleLogin


router = routers.DefaultRouter()
router.register("user", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("google/login", google_login, name="google_login"),
    path("google/callback/", google_callback, name="google_callback"),
    path("google/login/finish/", GoogleLogin.as_view(), name="google_login_todjango"),
]
