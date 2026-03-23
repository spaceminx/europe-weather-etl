import requests
from datetime import datetime, timedelta
from config import DAYS_BACK

def get_date_range():
    today = datetime.now()
    end_date = today.strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=DAYS_BACK)).strftime('%Y-%m-%d')
    return start_date, end_date



def transform_weather_data(raw_weather_data):
    cleaned_rows = []

    for row in raw_weather_data:
        country = row['country']
        capital = row['capital']
        date = row['date']
        temp_max = row['temperature_2m_max']
        temp_min = row['temperature_2m_min']
        prec_sum = row['precipitation_sum']
        wind_speed = row['wind_speed_10m_max']
        sunshine = row['sunshine_duration']


        cleaned_rows.append({
            "country": country,
            "capital": capital,
            "date": date,
            "temperature_max": float(temp_max) if temp_max is not None else None,
            "temperature_min": float(temp_min) if temp_min is not None else None,
            "precipitation_sum": float(prec_sum) if prec_sum is not None else None,
            "wind_speed_max": float(wind_speed) if wind_speed is not None else None,
            "sunshine_duration_hours": round(float(sunshine) / 3600, 2) if sunshine is not None else None,
        })
    return cleaned_rows
