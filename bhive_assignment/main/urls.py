from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('test', views.testapi, name='testapi'),

    path('bhive/login', views.LoginAPIView.as_view(), name='login'),

    path('bhive/register', views.RegisterUserAPIView.as_view(), name='register'),

    # path('bhive/fundschemes'),

    path('bhive/portfolio', views.PortfolioAPIView.as_view(), name='portfolio')
]