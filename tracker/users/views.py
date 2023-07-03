import json
from django.shortcuts import render
from rest_framework import viewsets, permissions, authentication
from .models import User
from .serializers import UserSerializer
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        password = request.data.get('password')
        if not password:
            return Response({'error': 'Password is required.'}, status=status.HTTP_400_BAD_REQUEST)

        return self.perform_create(request, *args, **kwargs)

    def perform_create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        token = Token.objects.create(user=user)
        return Response(json.dumps({"data": serializer.data, "token": token.key}), status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        name = data['name']
        password = data['password']
        user = User.objects.filter(name=name)
        if user:
            password_match = check_password(password, user[0].password)
        if password_match:
            try:
                token = Token.objects.get(user_id=user[0].id)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user[0])
            return JsonResponse({'token': token.key}, status=200)

        else:
            return JsonResponse({'error': 'error_message'}, status=400)
