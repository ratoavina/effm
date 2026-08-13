# /home/runner/work/effm/effm/src/effmapp/api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from effmapp.models.User import User
from .serializers import UserCreateSerializer, UserReadSerializer, UserUpdateSerializer

from django.shortcuts import get_object_or_404


class UserCreateAPIView(APIView):
    # permissions = [AllowAny]  # ou IsAdminUser selon ton besoin
    permissions = [IsAdminUser]

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "ok": True,
                "message": "Utilisateur créé",
                "data": UserReadSerializer(user).data
            },
            status=status.HTTP_201_CREATED
        )


class UserListAPIView(APIView):
    permission_classes = [IsAuthenticated]  # mieux que public

    def get(self, request):
        users = User.objects.all().order_by("id")
        data = UserReadSerializer(users, many=True).data
        return Response(
            {"ok": True, "count": len(data), "data": data},
            status=status.HTTP_200_OK
        )


class UserUpdateDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def put(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserUpdateSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {"ok": True, "message": "Utilisateur mis à jour", "data": UserReadSerializer(user).data},
            status=status.HTTP_200_OK
        )

    def patch(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {"ok": True, "message": "Utilisateur partiellement mis à jour", "data": UserReadSerializer(user).data},
            status=status.HTTP_200_OK
        )

    def delete(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return Response(
            {"ok": True, "message": "Utilisateur supprimé"},
            status=status.HTTP_200_OK
        )
