from django.shortcuts import render
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from main.serializers import RegisterUserSerializer, LoginSerializer, PortfolioSerializer
from rest_framework import status
from main.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from main.models import Portfolio
from rest_framework.generics import ListAPIView, ListCreateAPIView

# Create your views here.



import requests

url = "https://latest-mutual-fund-nav.p.rapidapi.com/master"

querystring = {"RTA_Agent_Code":"CAMS"}

headers = {
    'x-rapidapi-key': "de4ca0dcf4msh2ba6ec89fa54611p163c25jsn92cad99c880b",
    'x-rapidapi-host': "latest-mutual-fund-nav.p.rapidapi.com"
}

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())


AMC_CODES = {
    BirlaSunLifeMutualFund_MF,
    DSP_MF,
    SBIMutualFund_MF,
    TATAMutualFund_MF,
    FRANKLINTEMPLETON,
    PPFAS_MF,
    HSBCMUTUALFUND_MF
}

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
    

class PortfolioAPIView(ListCreateAPIView):

    permission_classes = [ IsAuthenticated, IsOwner ]
    serializer_class = PortfolioSerializer
    # parser_classes = [ MultiPartParser, FormParser ]
    queryset = Portfolio.objects.all()


    def perform_create(self,serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.filter(owner= self.request.user)
     