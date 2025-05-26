from datetime import datetime
import httpx


class WeatherServices:

    def get_coordinates(self, city_name: str) -> tuple[float, float] | None:
        url = "https://nominatim.openstreetmap.org/search"
        with httpx.Client(headers={"User-Agent": "weather-app"}) as client:
            response = client.get(url, params={
                "q": city_name,
                "format": "json",
                "limit": 1
            })
            data = response.json()
            if not data:
                return None
            return float(data[0]["lat"]), float(data[0]["lon"])

    def get_weather_forecast(self, lat: float, lon: float) -> dict:
        url = "https://api.open-meteo.com/v1/forecast"
        with httpx.Client() as client:
            response = client.get(url, params={
                "latitude": lat,
                "longitude": lon,
                "current_weather": True,
                "hourly": "temperature_2m",
                "timezone": "auto"
            })
            data = response.json()
            return self.format_weather_data(data)

    def format_weather_data(self, data: dict) -> dict:
        current = data.get("current_weather", {})
        hourly = data.get("hourly", {})

        result = {
            "Текущее состояние": {
                "Температура": f"{current.get('temperature', '?')} °C",
                "Скорость ветра": f"{current.get('windspeed', '?')} км/ч",
                "Время": datetime.fromisoformat(current.get("time")).strftime("%Y-%m-%d %H:%M") if current.get(
                    "time") else "Неизвестно"
            },
            "Прогноз на ближайшие часы": []
        }

        times = hourly.get("time", [])[:5]
        temperatures = hourly.get("temperature_2m", [])[:5]

        for time_str, temp in zip(times, temperatures):
            dt = datetime.fromisoformat(time_str)
            result["Прогноз на ближайшие часы"].append({
                "Время": dt.strftime("%Y-%m-%d %H:%M"),
                "Температура": f"{temp} °C"
            })

        return result
