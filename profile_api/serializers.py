import email
from pyexpat import model
from rest_framework import serializers
from . models import *


# Serializers

class HelloSerializer(serializers.Serializer):
    '''Serializes a name field for our APIView'''

    name = serializers.CharField(max_length=20)
    

class UserProfileSerializer(serializers.ModelSerializer):
    '''Serializes a User profile object'''
    class Meta:
        model = UserProfile
        fields = ('id', 'name', 'email', 'password') 
        extra_kwargs = {
            'password' : {
                'write_only': True,
                'style': { 'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        '''Create and return a new user'''

        user = models.User.objects.create_user(
            name=validated_data['name'],
            email=validated_data['email'],
            password=validated_data['password'],
        )

        return user

    