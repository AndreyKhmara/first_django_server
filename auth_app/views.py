from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class RegisterView(APIView):
    def post(self, request):
        login = request.data.get("login")
        password = request.data.get("password")

        if not login or not password:
            return Response({"error": "Missing login/password"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=login).exists():
            return Response({"error": "User already exist"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=login, password=password)

        return Response(
            {"message": "User created", "user_id": user.id},
            status=status.HTTP_201_CREATED
        )
