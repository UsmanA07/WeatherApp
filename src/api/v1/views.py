from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.weather.services.weather_api_services import WeatherServices


class WeatherView(APIView):
    service = WeatherServices()

    def get(self, request):
        city_name = request.query_params.get("city")
        if not city_name:
            return Response({"error": "City is required"}, status=status.HTTP_400_BAD_REQUEST)

        coords = self.service.get_coordinates(city_name)
        if coords is None:
            return Response(
                {"error": "Похоже, вы неправильно ввели название города"},
                status=status.HTTP_404_NOT_FOUND
            )

        forecast = self.service.get_weather_forecast(*coords)
        return Response(forecast)
