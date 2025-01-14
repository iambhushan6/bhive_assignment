from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('bhive/test', views.testapi, name='testapi'),

    path('bhive/login', views.LoginAPIView.as_view(), name='login'),

    path('bhive/register', views.RegisterUserAPIView.as_view(), name='register'),

    path('bhive/fundhouses', views.FundHouseListAPIView.as_view(), name='fund_houses'),

    path('bhive/fundhouse-schemes', views.FundHouseSchemeListAPIView.as_view(), name='fund_house_schemes'),

    path('bhive/portfolio/list', views.PortfolioListAPIView.as_view(), name='portfolio_list'),

    path('bhive/portfolio/create', views.PortfolioCreateAPIView.as_view(), name='portfolio_create')
]