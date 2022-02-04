import sqlite3
import requests
from pprint import pprint
import json

db = sqlite3.connect('weather.db')
cursor = db.cursor()
cursor.executescript(
    '''
    DROP TABLE IF EXISTS weather;
    CREATE TABLE IF NOT EXISTS weather(
    weather_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT,
    temp TEXT,
    wind TEXT);
    '''
)


db.commit()
db.close()
