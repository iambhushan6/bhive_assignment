from django.contrib import auth
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from main import models
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site

User = get_user_model()

class RegisterUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=60, min_length=6, write_only=True)

    class Meta:
        model = models.User
        fields = ['email', 'password', 'username', 'id']

    def validate(self, attrs):
        email = attrs.get('email','')
        username = attrs.get('username','')
        id = attrs.get('id','')
        _id = attrs.get('_id','')

        return attrs 

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):


    email = serializers.CharField()
    password = serializers.CharField(max_length = 68, min_length = 6, write_only = True)
    authToken = serializers.CharField(max_length = 68, min_length = 6, read_only=True)


    class Meta:
        model = models.User
        fields = ['email', 'password', 'authToken']

    def validate(self, attrs):
        email = attrs.get('email','')
        password = attrs.get('password','')
        user = auth.authenticate( email= email, password= password)

        if not user:
            raise AuthenticationFailed("Invalid Credentials")

        return {  
            "email": user.email,
            # "username": user.username,
            'authToken': user.tokens
        }
    

class PortfolioSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Portfolio
        fields = [
            "scheme_name",
            "scheme_code",
            "scheme_meta_data",
            "amount"
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        return models.Portfolio.objects.create(user=user, **validated_data)