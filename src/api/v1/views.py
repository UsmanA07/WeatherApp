from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.weather.services.weather_api_services import WeatherServices


class WeatherView(APIView):
    service = WeatherServices()

    def get(self, request):
        city_name = request.query_params.get("city")

        if not city_name:
            city_name = request.COOKIES.get("last_city")
            if not city_name:
                return Response(
                    {"error": "Город не указан и не найден в cookies"},
                    status=status.HTTP_400_BAD_REQUEST
                )

        coords = self.service.get_coordinates(city_name)
        if coords is None:
            return Response(
                {"error": "Похоже, вы неправильно ввели название города"},
                status=status.HTTP_404_NOT_FOUND
            )

        forecast = self.service.get_weather_forecast(*coords)
        response = Response(forecast)
        max_age = 30 * 24 * 60 * 60
        if request.query_params.get("city"):
            response.set_cookie("last_city", city_name, max_age=max_age)

        return response


class AutocompleteCityView(APIView):
    service = WeatherServices()

    def get(self, request):
        query = request.query_params.get("query")
        if not query:
            return Response({"error": "Query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        results = self.service.autocomplete_city(query)
        return Response(results)
