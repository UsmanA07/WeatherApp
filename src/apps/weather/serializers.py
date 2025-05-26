from rest_framework import serializers
from apps.weather.models import City


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name']


class StatsSerializer(serializers.Serializer):
    city = serializers.CharField()
    count = serializers.IntegerField()
