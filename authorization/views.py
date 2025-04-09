from django.shortcuts import render
from rest_framework.views import APIView
from .models import CustomUser
from .serializer import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import TokenSerializer

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Регистрация прошла успешно"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TokenView(TokenObtainPairView):
    serializer_class = TokenSerializer