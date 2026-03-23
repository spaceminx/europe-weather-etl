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
        daily = row['raw_daily_data']
        for date, temp_max, temp_min, prec_sum, wind_speed, sun_dur in zip(
            daily["time"],
            daily["temperature_2m_max"],
            daily["temperature_2m_min"],
            daily["precipitation_sum"],
            daily["wind_speed_10m_max"],
            daily["sunshine_duration"],
        ):
            cleaned_rows.append({
                "country": country,
                "capital_name": capital,
                "date": date,
                "temperature_max": float(temp_max) if temp_max is not None else None,
                "temperature_min": float(temp_min) if temp_max is not None else None,
                "precipitation_sum": float(prec_sum) if prec_sum is not None else None,
                "wind_speed_max": float(wind_speed) if wind_speed is not None else None,
                "sunshine_duration": round(float(sun_dur) / 3600, 2) if sun_dur is not None else None,
            })
    return cleaned_rows
