from src.extract import fetch_countries, fetch_weather, extract_capitals
from src.transform import transform_weather_data, get_date_range
from src.load import load_raw_data, load_clean_data, get_raw_data
from src.db import create_raw_table, create_clean_table
from src.views import create_views


def main():
    create_raw_table()
    create_clean_table()


    countries_data = fetch_countries()
    capitals = extract_capitals(countries_data)

    start_date, end_date = get_date_range()

    raw_weather = fetch_weather(capitals, start_date, end_date)
    load_raw_data(raw_weather)

    raw_rows = get_raw_data()
    clean_weather = transform_weather_data(raw_rows)

    load_clean_data(clean_weather)
    create_views()
    print("\n--------------------------------")
    print("Pipeline completed successfully.")
    print("--------------------------------\n")

if __name__ == '__main__':
    main()