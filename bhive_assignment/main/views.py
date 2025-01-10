from django.shortcuts import render
from rest_framework.decorators import api_view, APIView

# Create your views here.




import requests

url = "https://latest-mutual-fund-nav.p.rapidapi.com/master"

querystring = {"AMC_Code":"PP001ZG","RTA_Agent_Code":"CAMS"}

headers = {
	"x-rapidapi-key": "b260ddb945msh39a03fb3d0984a8p15f4dfjsnc99fcc61ea15",
	"x-rapidapi-host": "latest-mutual-fund-nav.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())




@api_view()
def testapi(request):
    return Response({'Bhushan':'Its Working!'})