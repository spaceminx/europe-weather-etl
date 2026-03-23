import requests
from config import RESTCOUNTRIES_API_URL, OPENMETEO_API_URL



def fetch_countries():
    response = requests.get(RESTCOUNTRIES_API_URL)
    response.raise_for_status()
    return response.json()


def extract_capitals(data):
    results = []

    for country in data:
        country_name = country['name']['common']
        capital_name = country.get('capital', [None])[0]
        capital_lat, capital_lng = country.get('capitalInfo', {}).get('latlng', [None, None])

        if not capital_name or not capital_lat or not capital_lng:
            continue

        results.append({
            'country': country_name,
            'capital': capital_name,
            'lat': capital_lat,
            'lng': capital_lng
        })
    return results


def fetch_weather(capitals, start_date, end_date):
    weather_data = []

    for capital in capitals:
        params = {
            "latitude" : capital["lat"],
            "longitude" : capital["lng"],
            "start_date" : start_date,
            "end_date" : end_date,
            "daily" : [
                "temperature_2m_max",
                "temperature_2m_min",
                "precipitation_sum",
                "wind_speed_10m_max",
                "sunshine_duration",
            ]
        }

        response = requests.get(OPENMETEO_API_URL, params=params)
        response.raise_for_status()

        data = response.json()

        weather_data.append({
            "country": capital["country"],
            "capital": capital["capital"],
            "lat": capital["lat"],
            "lng": capital["lng"],
            "raw_daily_data": data["daily"],
        })

    return weather_data