import sqlite3
from config import DATABASE_PATH


def get_connection():
    return sqlite3.connect(DATABASE_PATH)


def create_clean_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS clean_weather(
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
        )
    ''')
    conn.commit()
    conn.close()

def create_raw_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS raw_weather(
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
        )
    ''')
    conn.commit()
    conn.close()