from django.urls import path
from .views import create_user
from .views import get_users

urlpatterns = [
    path("users/", create_user, name="api_create_user"),
    path("users/get/", get_users, name="api_get_users")
]