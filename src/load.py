import sqlite3

from src.db import get_connection

def get_raw_data():
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute('SELECT * FROM raw_weather')
    rows = cur.fetchall()

    conn.close()
    return rows


def load_clean_data(weather_rows):
    conn = get_connection()
    cur = conn.cursor()

    for row in weather_rows:
        cur.execute('''
            INSERT INTO clean_weather(
                country, capital, date, temperature_max,
                temperature_min, precipitation_sum, wind_speed_max,
                sunshine_duration_hours
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT (capital, date) DO UPDATE SET
                temperature_max = EXCLUDED.temperature_max,
                temperature_min = EXCLUDED.temperature_min,
                precipitation_sum = EXCLUDED.precipitation_sum,
                wind_speed_max = EXCLUDED.wind_speed_max,
                sunshine_duration_hours = EXCLUDED.sunshine_duration_hours
        ''', (
              row['country'],
              row['capital'],
              row['date'],
              row['temperature_max'],
              row['temperature_min'],
              row['precipitation_sum'],
              row['wind_speed_max'],
              row['sunshine_duration_hours']
              ))
    conn.commit()
    conn.close()


def load_raw_data(raw_rows):
    conn = get_connection()
    cur = conn.cursor()

    for row in raw_rows:
        daily = row['raw_daily_data']

        for date, temp_max, temp_min, prec_sum, wind_speed, sunshine in zip(
                daily['time'],
                daily['temperature_2m_max'],
                daily['temperature_2m_min'],
                daily['precipitation_sum'],
                daily['wind_speed_10m_max'],
                daily['sunshine_duration']
        ):
            cur.execute('''
            INSERT INTO raw_weather(
                country,
                capital,
                date,
                temperature_2m_max,
                temperature_2m_min,
                precipitation_sum,
                wind_speed_10m_max,
                sunshine_duration
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT (capital, date) DO UPDATE SET
                temperature_2m_max = EXCLUDED.temperature_2m_max,
                temperature_2m_min = EXCLUDED.temperature_2m_min,
                precipitation_sum = EXCLUDED.precipitation_sum,
                wind_speed_10m_max = EXCLUDED.wind_speed_10m_max,
                sunshine_duration = EXCLUDED.sunshine_duration
            ''', (
                row['country'],
                row['capital'],
                date,
                temp_max,
                temp_min,
                prec_sum,
                wind_speed,
                sunshine
            ))

    conn.commit()
    conn.close()