from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'bio']


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        modal = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
