import requests
from datetime import datetime, timedelta
from config import RESTCOUNTRIES_API_URL, OPENMETEO_API_URL, DAYS_BACK

r = requests.get(RESTCOUNTRIES_API_URL)

countries_data = r.json()

'''
    30 days:
      max/min temp: temperature_2m_max, temperature_2m_min (degree C)
      precipation sum: precipitation_sum(mm)
      max windspeed: wind_speed_10m_max (km/h)
      sunshine duration: sunshine_duration(seconds)
'''


today = datetime.now()
end_date = today.strftime('%Y-%m-%d')
start_date = (today - timedelta(days=DAYS_BACK)).strftime('%Y-%m-%d')



def fetch_weather(capitals, start_date, end_date):
    weather_rows = []

    for capital in capitals:
        country_name = capital["country"]
        capital_name = capital["capital"]
        capital_lat = capital["lat"]
        capital_lng = capital["lng"]


        params = {
            "latitude" : capital_lat,
            "longitude" : capital_lng,
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
        data = response.json()
        daily = data["daily"]
        time = daily["time"]

        for date, temp_max, temp_min, prec_sum, wind_speed, sun_dur in zip(
            daily["date"],
            daily["temperature_2m_max"],
            daily["temperature_2m_min"],
            daily["precipitation_sum"],
            daily["wind_speed_10m_max"],
            daily["sunshine_duration"],
        ):
            weather_rows.append({
                "country": country_name,
                "capital_name": capital_name,
                "date": date,
                "temperature_max": temp_max,
                "temperature_min": temp_min,
                "precipitation_sum": prec_sum,
                "wind_speed_max": wind_speed,
                "sunshine_duration": sun_dur,
            })
    return weather_rows







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

capitals = extract_capitals(countries_data)


fetch_weather(capitals, start_date, end_date)
#print(start_date, end_date)
#print(weather_datas)

