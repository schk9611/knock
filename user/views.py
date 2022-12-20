import os

from django.shortcuts import redirect

from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer


state = os.environ.get("STATE")
BASE_URL = "http://localhost:8000/"
GOOGLE_CALLBACK_URI = BASE_URL + "user/google/callback/"


def google_login(request):
    """
    client_id, redirect_uri, scope 등의 정보를 url parameter로 함께 보내 리다이렉트한다.
    실행 결과로 구글 로그인 창이 뜨고, 알맞은 아이디, 비밀번호로 진행하면 Callback URI로 Code 값이 들어간다.
    """
    scope = "https://www.googleapis.com/auth/userinfo.email"
    client_id = os.environ.get("SOCIAL_AUTH_GOOGLE_CLIENT_ID")
    return redirect(
        f"https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&response_type=code&redirect_uri={GOOGLE_CALLBACK_URI}&scope={scope}"
    )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
