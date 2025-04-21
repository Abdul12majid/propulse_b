from django.shortcuts import render, HttpResponse
from django.contrib.auth import login, logout, authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer, SignUpSerializer
from django.contrib.auth.models import User

# Create your views here.
@api_view(['POST'])
def login_user(request):
	serializer = LoginSerializer(data=request.data)
	if serializer.is_valid():
		username = request.data['username']
		password = request.data['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return Response({'Info': 'Login Successful'})
		else:
			return Response({'Info': 'Incorrect username or password'})

	return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])	
def register(request):
	serializer = SignUpSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		response = {
			"info":"Registeration successful",
			"user info":serializer.data
		}
		return Response(data=response, status=status.HTTP_201_CREATED)
	return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])	
def logout_user(request):
	logout(request)
	return Response({'Info': "You've been logged out"})


@api_view(['POST', 'GET'])
def bookmarked(request, username):
	user = User.objects.get(username=username)
	user_profile = user.profile
	hostels = user_profile.bookmarked.all()
	serializer = HostelSerializer(hostels, many=True)
	return Response({'Your Bookmarks': serializer.data})