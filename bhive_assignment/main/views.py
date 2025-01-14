from django.shortcuts import render
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from main.serializers import RegisterUserSerializer, LoginSerializer, PortfolioSerializer
from rest_framework import status
from main.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from main.models import Portfolio, FundHouse, AMC_CODES
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView
from main.services import BhiveFundService

# Create your views here.


@api_view()
def testapi(request):
    return Response({'Hello':'Its Working!'})



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
    

class FundHouseListAPIView(ListAPIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(FundHouse.objects.all() or AMC_CODES, status= status.HTTP_200_OK)


class FundHouseSchemeListAPIView(GenericAPIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        amc_code = request.query_params.get("amc_code")
        if not amc_code:
            return Response({"Error": "Please enter amc code parameter"}, status= status.HTTP_400_BAD_REQUEST)
        is_success, data_or_error = BhiveFundService().get_fund_house_schemes(fund_house=amc_code)
        if not is_success:
            return Response({"Error": data_or_error}, status= status.HTTP_400_BAD_REQUEST)
        return Response({"data":data_or_error}, status=status.HTTP_200_OK)


class PortfolioCreateAPIView(CreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class PortfolioListAPIView(ListAPIView):
    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Portfolio.objects.filter(user=self.request.user)
     