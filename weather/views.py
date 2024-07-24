# weather/views.py

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import logging
from django.conf import settings
from .serializers import WeatherSerializer

logger = logging.getLogger(__name__)

def weather_form(request):
    return render(request, 'weather_form.html')

class WeatherAPIView(APIView):
    def get(self, request, city):
        api_key = settings.OPENWEATHERMAP_API_KEY
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

        logger.debug(f"Requesting weather data for {city} with URL: {complete_url}")

        response = requests.get(complete_url)
        logger.debug(f"Response status code: {response.status_code}")
        logger.debug(f"Response content: {response.text}")

        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "city": data['name'],
                "temperature": data['main']['temp'],
                "description": data['weather'][0]['description'],
                "forecast": self.get_forecast(city)
            }
            serializer = WeatherSerializer(weather_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif response.status_code == 401:
            logger.error("Invalid API key")
            return Response({"error": "Invalid API key"}, status=status.HTTP_401_UNAUTHORIZED)
        elif response.status_code == 404:
            logger.error("City not found")
            return Response({"error": "City not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            logger.error(f"Unexpected error: {response.status_code}")
            return Response({"error": "An unexpected error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_forecast(self, city):
        api_key = settings.OPENWEATHERMAP_API_KEY
        base_url = "http://api.openweathermap.org/data/2.5/forecast?"
        complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

        logger.debug(f"Requesting weather forecast for {city} with URL: {complete_url}")

        response = requests.get(complete_url)
        logger.debug(f"Forecast response status code: {response.status_code}")
        logger.debug(f"Forecast response content: {response.text}")

        if response.status_code == 200:
            data = response.json()
            forecast_list = []
            for forecast in data['list']:
                forecast_data = {
                    "date": forecast['dt_txt'],
                    "temperature": forecast['main']['temp'],
                    "description": forecast['weather'][0]['description']
                }
                forecast_list.append(forecast_data)
            return forecast_list
        else:
            logger.error("Failed to get forecast")
            return []

def index(request):
    return render(request, 'weather_form.html')