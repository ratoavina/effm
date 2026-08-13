# /home/runner/work/effm/effm/src/effmapp/api/urls.py
from django.urls import path
from .views import UserCreateAPIView, UserListAPIView, UserUpdateDeleteAPIView

urlpatterns = [
    path("users/create/", UserCreateAPIView.as_view(), name="api_users_create"),
    path("users/get/", UserListAPIView.as_view(), name="api_users_get"),
    path("users/update/<int:user_id>/", UserUpdateDeleteAPIView.as_view(), name="api_users_update"),
    path("users/delete/<int:user_id>/", UserUpdateDeleteAPIView.as_view(), name="api_users_delete"),
]