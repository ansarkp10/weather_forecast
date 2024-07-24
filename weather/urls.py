# weather/urls.py
from django.urls import path
from .views import WeatherAPIView, index

urlpatterns = [
    path('', index, name='weather_form'),
    path('weather/<str:city>/', WeatherAPIView.as_view(), name='weather'),
]
