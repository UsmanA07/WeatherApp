from django.urls import path
from api.v1.views import WeatherView, AutocompleteCityView

urlpatterns = [
    path('weather/', WeatherView.as_view(), name='weather'),
    path("weather/autocomplete/", AutocompleteCityView.as_view()),
]