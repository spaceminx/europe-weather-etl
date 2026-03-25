CREATE TABLE raw_weather(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        country TEXT NOT NULL,
        capital TEXT NOT NULL,
        date TEXT NOT NULL,
        temperature_2m_max REAL,
        temperature_2m_min REAL,
        precipitation_sum REAL,
        wind_speed_10m_max REAL,
        sunshine_duration REAL,
        UNIQUE(capital, date)
        );
CREATE TABLE clean_weather(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        country TEXT NOT NULL,
        capital TEXT NOT NULL,
        date TEXT NOT NULL,
        temperature_max REAL,
        temperature_min REAL,
        precipitation_sum REAL,
        wind_speed_max REAL,
        sunshine_duration_hours REAL,
        UNIQUE(capital, date)
        );
CREATE VIEW avg_temperature_by_capital AS
    SELECT capital, country, ROUND(AVG(temperature_max), 1) AS avg_temperature
    FROM clean_weather
    GROUP BY capital, country
    ORDER BY avg_temperature DESC
/* avg_temperature_by_capital(capital,country,avg_temperature) */;
CREATE VIEW rainfall_by_country AS
    SELECT country, ROUND(SUM(precipitation_sum), 2) as rainfall
    FROM clean_weather
    GROUP BY country
    ORDER BY rainfall DESC
/* rainfall_by_country(country,rainfall) */;
CREATE VIEW country_30_day_summary AS
    SELECT
        country,
        ROUND(AVG(temperature_max), 1) AS avg_temperature_max,
        ROUND(AVG(temperature_min), 1) AS avg_temperature_min,
        ROUND(SUM(precipitation_sum), 2) AS total_precipitation,
        ROUND(AVG(wind_speed_max), 1) AS avg_wind_speed,
        ROUND(SUM(sunshine_duration_hours), 1) as total_sunshine_hours
    FROM clean_weather
    GROUP BY country
/* country_30_day_summary(country,avg_temperature_max,avg_temperature_min,total_precipitation,avg_wind_speed,total_sunshine_hours) */;
