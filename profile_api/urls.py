from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    # index function
    path('', views.index, name='index'),

]