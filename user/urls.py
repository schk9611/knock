from rest_framework import routers
from django.urls import path, include

from .views import (
    UserViewSet,
    google_login,
    google_callback,
    GoogleLogin,
    kakao_login,
    kakao_callback,
    KakaoLogin,
)


router = routers.DefaultRouter()
router.register("", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # 구글 소셜 로그인
    path("google/login", google_login, name="google_login"),
    path("google/callback/", google_callback, name="google_callback"),
    path("google/login/finish/", GoogleLogin.as_view(), name="google_login_todjango"),
    # 카카오 소셜 로그인
    path("kakao/login/", kakao_login, name="kakao_login"),
    path("kakao/callback/", kakao_callback, name="kakao_callback"),
    path("kakao/login/finish/", KakaoLogin.as_view(), name="kakao_login_todjango"),
]
