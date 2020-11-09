"""opr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from frontend.views import *
from .views import *

urlpatterns = [
    path('dashboard/', Home.as_view(), name='dashboard'),
    path('index/<pk>/', IndexUpdateView.as_view(), name='index'),
    path('about/<pk>/', AboutUpdateView.as_view(), name='about'),
    path('vision/<pk>/', VisionUpdateView.as_view(), name='vision'),
    path('events/<pk>/', EventsUpdateView.as_view(), name='events'),
    path('contact_list/', ContactListView.as_view(), name='contact_list'),
    path('contact_message/<pk>/', ContactMessageView.as_view(), name='contact_message'),
    path('message_delete/<pk>/', DeleteMessageView.as_view(), name='message_delete'),
    path('registred-user/', RegistrationListView.as_view(), name='registred-user'),

]
