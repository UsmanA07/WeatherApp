import asyncio

from rest_framework.response import Response
from rest_framework.views import APIView
from apps.weather.services.weather_api_services import WeatherServices


class WeatherView(APIView):
    def get(self, request):
        city_name = request.query_params.get("city")
        services = WeatherServices()
        coords = asyncio.run(services.get_coordinates(city_name))

        inf = asyncio.run(services.get_weather_forecast(coords[0], coords[1]))
        inf1 = services.format_weather_data(inf)
        return Response(inf)
