from src.db import get_connection

def create_views():
    conn = get_connection()
    cur = conn.cursor()

    cur.executescript('''
    CREATE VIEW IF NOT EXISTS avg_temperature_by_capital AS
    SELECT capital, country, ROUND(AVG(temperature_max), 1) AS avg_temperature
    FROM clean_weather
    GROUP BY capital, country
    ORDER BY avg_temperature DESC;
    
    CREATE VIEW IF NOT EXISTS rainfall_by_country AS
    SELECT country, ROUND(SUM(precipitation_sum), 2) as rainfall
    FROM clean_weather
    GROUP BY country
    ORDER BY rainfall DESC;
    
    CREATE VIEW IF NOT EXISTS country_30_day_summary AS
    SELECT
        country,
        ROUND(AVG(temperature_max), 1) AS avg_temperature_max,
        ROUND(AVG(temperature_min), 1) AS avg_temperature_min,
        ROUND(SUM(precipitation_sum), 2) AS total_precipitation,
        ROUND(AVG(wind_speed_max), 1) AS avg_wind_speed,
        ROUND(SUM(sunshine_duration_hours), 1) as total_sunshine_hours
    FROM clean_weather
    GROUP BY country;
    ''')

    conn.commit()
    conn.close()