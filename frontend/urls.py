from django.urls import path, include

from frontend.views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('aboutus/', About.as_view(), name='aboutus'),
    path('vision&mission/', Vision.as_view(), name='visionmission'),
    path('event/', Events.as_view(), name='event'),
    path('contactus/', ContactUS.as_view(), name='contactus'),
    ]

