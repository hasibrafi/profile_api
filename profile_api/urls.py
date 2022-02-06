from unicodedata import name
from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')  

urlpatterns = [ 
    # index function
    path('', views.index, name='index'),

    # URL's for API Views
    path('api/hello-view/', views.HelloApiView.as_view()),
    
    # URL's for ViewSets
    path('', include(router.urls))
]