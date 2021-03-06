"""itorre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from rest_framework.authtoken import views

from ios.api import OsViewSet

app_name = 'ios'
router = routers.DefaultRouter()
router.register('',OsViewSet) #nome da rota

urlpatterns = [
    path('api/', include(router.urls)),
    # + [url('auth',views.obtain_auth_token)])),
    # a rota de cima usava o token padrão agora
    # toda a API vai usar token JWT tendo autenticação
    # por apenas uma rota auth-api
]