from django.shortcuts import render
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from main.serializers import RegisterUserSerializer, LoginSerializer
from rest_framework import status

# Create your views here.




import requests

url = "https://latest-mutual-fund-nav.p.rapidapi.com/master"

querystring = {"AMC_Code":"PP001ZG","RTA_Agent_Code":"CAMS"}

headers = {
	"x-rapidapi-key": "b260ddb945msh39a03fb3d0984a8p15f4dfjsnc99fcc61ea15",
	"x-rapidapi-host": "latest-mutual-fund-nav.p.rapidapi.com"
}

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())




@api_view()
def testapi(request):
    return Response({'Bhushan':'Its Working!'})



class RegisterUserAPIView(GenericAPIView):
    
    serializer_class = RegisterUserSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        return Response(user_data, status= status.HTTP_201_CREATED)
    

class LoginAPIView(GenericAPIView):
    
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        
        return Response(serializer.data, status= status.HTTP_200_OK)
     