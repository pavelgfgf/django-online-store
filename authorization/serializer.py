from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    
    class Meta:
        model = CustomUser
        fields = ['email', 'password'] 

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            username=validated_data.get('username', '')
        )
        return user

class TokenSerializer(TokenObtainPairSerializer): 
    def validate(self, attrs):
        data = super().validate(attrs)

        data.pop('refresh', None)

        data['token'] = data.pop('access')

        return data