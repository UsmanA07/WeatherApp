from django.urls import path
from api.v1.views import WeatherView

urlpatterns = [
    path('weather/', WeatherView.as_view(), name='weather'),
]