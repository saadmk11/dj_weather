import requests

from django.conf import settings


def get_weather_data(latitude, longitude):
    api_url = settings.WEATHER_API_URL
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64;"
    }
    response = requests.get(
        api_url,
        headers=headers,
        params={'lat': latitude, 'lon': longitude}
    )

    if response.status_code == 200:
        response_data = response.json()
        return (True, response_data['properties']['timeseries'][0]['data'])
    else:
        return (
            False,
            {'error': 'An Error occurred while getting weather information'}
        )
