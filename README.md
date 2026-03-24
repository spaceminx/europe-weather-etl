## Running the Pipeline

### 1. Clone the repository
```
git clone https://github.com/spaceminx/europe-weather-etl.git

cd europe-weather-etl
```

### 2. Create a virtual environment
```
python -m venv .venv

```

### 3. Activate the virtual environment

- On macOS/Linux:
```
source .venv/bin/activate

```

- On Windows:
```
.venv\Scripts\activate

```

### 4. Install dependencies
```
pip install -r requirements.txt

```

### 5. Run the pipeline
```
python main.py

```

## Viewing the Database

The SQLite database file is created automatically at:

database/weather.sqlite


You can open it using any SQLite client for example:
- DB Browser
- SQLite CLI:
  ```
  sqlite3 database/weather.sqlite
  ```
