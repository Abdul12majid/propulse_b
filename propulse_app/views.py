from django.shortcuts import render, HttpResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import HostelMedia, Hostel, Address
from .serializers import HostelMediaSerializer, HostelSerializer, MessageSerializer
from rest_framework.decorators import api_view, parser_classes, permission_classes
from django.urls import reverse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

# Create your views here.

@api_view(['GET'])
def root(request, format=None):
    return Response({
        'All Hostels': request.build_absolute_uri(reverse('all_hostels', args=[], kwargs={})),
        'Available Hostels': request.build_absolute_uri(reverse('available_hostels', args=[], kwargs={})),
        'Create Hostel': request.build_absolute_uri(reverse('create_hostel', args=[], kwargs={})),
        'Search hostels': request.build_absolute_uri(reverse('search_hostels', kwargs={'address': '<address-value>'})),
        'Send message': request.build_absolute_uri(reverse('send_message', args=[], kwargs={})),
        'Login user': request.build_absolute_uri(reverse('login', args=[], kwargs={})),
        'Logout user': request.build_absolute_uri(reverse('logout', args=[], kwargs={})),
        'Register user': request.build_absolute_uri(reverse('register', args=[], kwargs={})),
        
    })



@api_view(['GET'])
def all_hostels(request):
    hostels = Hostel.objects.all()

    #filtering
    filter_backend = DjangoFilterBackend()
    hostels = filter_backend.filter_queryset(request, hostels, view=None)
    filter_backend.filterset_fields = ['name']

    # Apply search
    search_backend = SearchFilter()
    search_backend.search_fields = ['name']
    hostels = search_backend.filter_queryset(request, hostels, view=None)

    # Apply pagination
    paginator = PageNumberPagination()
    paginator.page_size = 2
    paginated_hostels = paginator.paginate_queryset(hostels, request)

    # Serialize data
    serializer = HostelSerializer(hostels, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def available_hostels(request):
	all_hostels = Hostel.objects.filter(available=True).all()
	serializer = HostelSerializer(all_hostels, many=True)
	return Response({'data': serializer.data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
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


@api_view(['GET'])
def search_hostels(request, address):
    matching_addresses = Address.objects.filter(name__icontains=address).all()
    
    if matching_addresses:
    	hostels = Hostel.objects.filter(address__in=matching_addresses).all()
    	serializer = HostelSerializer(hostels, many=True)
    	return Response({'data': serializer.data})

    else:
	    return Response({'data': 'not found'})