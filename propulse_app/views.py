from django.shortcuts import render, HttpResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import HostelMedia, Hostel
from .serializers import HostelMediaSerializer, HostelSerializer, MessageSerializer
from rest_framework.decorators import api_view, parser_classes, permission_classes
from django.urls import reverse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['GET'])
def root(request, format=None):
    return Response({
        'All Hostels': request.build_absolute_uri(reverse('all_hostels', args=[], kwargs={})),
        'Available Hostels': request.build_absolute_uri(reverse('available_hostels', args=[], kwargs={})),
        'Create Hostel': request.build_absolute_uri(reverse('create_hostel', args=[], kwargs={})),
        'Send message': request.build_absolute_uri(reverse('send_message', args=[], kwargs={})),
    })



@api_view(['GET'])
def all_hostels(request):
	all_hostels = Hostel.objects.all()
	serializer = HostelSerializer(all_hostels, many=True)
	return Response({'data': serializer.data})


@api_view(['GET'])
def available_hostels(request):
	all_hostels = Hostel.objects.filter(available=True).all()
	serializer = HostelSerializer(all_hostels, many=True)
	return Response({'data': serializer.data})


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def create_hostel(request):
    serializer = HostelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_message(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(sender=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)