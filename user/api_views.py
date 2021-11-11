from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .serializers import *


@api_view(['POST'])
def user_register_api_view(request):
    if request.method == 'POST':
        print(request.data)
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return Response(serializer.data, 'User Successfully Register')
        else:
            return Response(serializer.errors, 'An error occurred during registration')


@api_view(['POST'])
def user_login_api_view(request):
    if request.user.is_authenticated:
        return Response('User Already Login')
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except:
            return Response('User dost exit')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return Response('User login successfully')
        else:
            return Response('Email and password does not exit')


@login_required(login_url='login-view')
@api_view(['POST'])
def update_user_api_view(request):
    user = request.user
    serializer = UserSerializer(instance=user)
    if request.method == 'POST':
        serializer = UserSerializer(request.POST, request.FILES, instance=user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 'User Edit Successfully')
        else:
            return Response(serializer.errors, 'Some error occur')


@api_view(['GET'])
def get_all_user_api_view(request):
    if request.method == 'GET':
        user = User.objects.all()
        return Response(user)
