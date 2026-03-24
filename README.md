## ETL Pipeline

The pipeline follows a standard ETL approach:

- **Extract**: Fetches European countries and capital coordinates from RestCountries, then retrieves weather data from Open-Meteo.
- **Transform**: Cleans the data (rounding, type conversions, handling missing values, converting sunshine duration from seconds to hours).
- **Load**: Stores raw data in a staging table and cleaned data in a final table.

## Database Design

Tables:

- **raw_weather**: stores raw fetched data
- **clean_weather**: stores cleaned and transformed data
 
While not required for small pipeline, staging table makes the pipeline more scalable for the future.

SQLite was chosen because it is simple to use and does not require any additional setup.

## Running the Pipeline with Docker

> **Note:** Make sure Docker is installed and running.

### 1. Clone the repository
```
git clone https://github.com/spaceminx/europe-weather-etl.git
```
```
cd europe-weather-etl
```

### 2. Build and run the pipeline

```
docker compose up --build
```

## Viewing the Database

The SQLite database file is created automatically at:

database/weather.sqlite


You can open it using any SQLite client or IDE

- SQLite CLI:
  ```
  sqlite3 database/weather.sqlite
  ```
