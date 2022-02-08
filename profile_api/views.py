from email import message
import imp
from operator import imod
import re
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from . import serializers
from . import models 

# Create your views here.

def index(request):
    return HttpResponse('Hello World! You are at index page..')

class HelloApiView(APIView):
    '''Test API View'''

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        '''Returns a list of APIView features'''

        an_apiview = [
            'This is the first line',
            'This is the second line',
            'This is the third line',
            'This is the fourth line',
        ]
        return Response({'an_apiview': an_apiview})

    def post(self, request):
        '''Create a hello message with a name'''

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        '''For updating an object'''

        return Response({'Method':'PUT'})

    
    def patch(self, request, pk=None):
        '''For partially updating an object'''

        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        '''For deleting an object'''

        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    '''Test API ViewSet'''

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        '''Return a hello message'''

        a_viewset = [
            'Users action (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Reuters',
            'Provides mpre functionality with less code',
        ]

        return Response({'message':'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        '''Create a new hello message'''

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        '''Handle getting an object by the ID'''

        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        '''Handle updating an object by the ID'''

        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        '''Handle partially-updating an object by the ID'''

        return Response({'http_method':'Patch'})

    def destroy(self, request, pk=None):
        '''Handle destroying an object by the ID'''

        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    '''Handle creating and updating profiles'''

    serializer_class = serializers.UserProfileSerializer

    queryset = models.UserProfile.objects.all()
     



