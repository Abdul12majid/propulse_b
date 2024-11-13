from django.shortcuts import render, HttpResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import HostelMedia, Hostel
from .serializers import HostelMediaSerializer, HostelSerializer
from rest_framework.decorators import api_view
from django.urls import reverse

# Create your views here.

@api_view(['GET'])
def root(request, format=None):
    return Response({
        'All Hostels': request.build_absolute_uri(reverse('all_hostels', args=[], kwargs={})),
    })



@api_view(['GET'])
def all_hostels(request):
	all_hostels = Hostel.objects.all()
	serializer = HostelSerializer(all_hostels, many=True)
	return Response({'data': serializer.data})