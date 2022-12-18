from rest_framework import routers
from django.urls import path, include

from .views import UserViewSet


router = routers.DefaultRouter()
router.register("user", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
