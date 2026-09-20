import requests


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


def get_coordinates(city):
    """Convert a city name into latitude/longitude."""

    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(
        GEOCODING_URL,
        params=params,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    if "results" not in data:
        raise ValueError(f"Location not found: {city}")

    result = data["results"][0]

    return {
        "city": city,
        "latitude": result["latitude"],
        "longitude": result["longitude"],
        "timezone": result.get("timezone")
    }


def get_weather_data(
    city,
    latitude,
    longitude,
    forecast_days=7
):
    """Extract hourly weather data from Open-Meteo."""

    params = {
        "latitude": latitude,
        "longitude": longitude,

        "hourly": ",".join([
            "temperature_2m",
            "relative_humidity_2m",
            "apparent_temperature",
            "precipitation_probability",
            "precipitation",
            "rain",
            "weather_code",
            "cloud_cover",
            "wind_speed_10m"
        ]),

        "forecast_days": forecast_days,
        "timezone": "auto"
    }

    response = requests.get(
        WEATHER_URL,
        params=params,
        timeout=30
    )

    response.raise_for_status()

    return response.json()
