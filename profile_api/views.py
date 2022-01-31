import imp
from operator import imod
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

def index(request):
    return HttpResponse('Hello World! You are at index page..')

class HelloApiView(APIView):
    '''Test API View'''

    def get(self, request, format=None):
        '''Returns a list of API View features'''

        an_apiview = [
            'This is the first line',
            'This is the second line',
            'This is the third line',
            'This is the fourth line',
        ]

        return Response({'an_apiview':an_apiview})
