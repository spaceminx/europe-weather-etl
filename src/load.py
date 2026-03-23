from src.db import get_connection

def load_data(weather_rows):
    conn = get_connection()
    cur = conn.cursor()

    for row in weather_rows:
        cur.execute('''
            INSERT OR IGNORE INTO weather_data (
                country, capital, date, temperature_max,
                temperature_min, precipitation_sum, wind_speed_max,
                sunshine_duration
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (row['country'],
              row['capital_name'],
              row['date'],
              row['temperature_max'],
              row['temperature_min'],
              row['precipitation_sum'],
              row['wind_speed_max'],
              row['sunshine_duration']
              ))
    conn.commit()
    conn.close()