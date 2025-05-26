from dataclasses import dataclass

from apps.weather.models import City


@dataclass
class PostListDTO:
    city: City