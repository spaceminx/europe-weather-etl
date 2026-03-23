from src.extract import fetch_countries, fetch_weather, extract_capitals
from src.transform import transform_weather_data, get_date_range
from src.load import load_data
from src.db import create_table


def main():
    create_table()


    countries_data = fetch_countries()
    capitals = extract_capitals(countries_data)

    start_date, end_date = get_date_range()
    raw_weather_data = fetch_weather(capitals, start_date, end_date)
    clean_weather_data = transform_weather_data(raw_weather_data)

    print(clean_weather_data[:1])
    load_data(clean_weather_data)

if __name__ == '__main__':
    main()