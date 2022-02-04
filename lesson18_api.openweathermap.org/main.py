import sqlite3
from pprint import pprint
import requests

db = sqlite3.connect('lesson18db.db')  # Bazaga ulanish
cursor = db.cursor()
# Один запрос
# Несколько запросов

# cursor.execute('''
#     SELECT * FROM customers;
# ''')
#
# customers = cursor.fetchall()  # Позволит взять все
# # fetchone() - взятие одного значения
# pprint(customers)

cursor.executescript('''
    DROP TABLE IF EXISTS user;
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT);
''')

# Чтобы отправить данные
db.commit()
db.close()

weather = sqlite3.connect('weather.db')
cursor = weather.cursor()

params = {
    'appid': 'd0c4c1e4babd454e692db213ba832310',  # myAPI keys in openweathermap.org
    'units': 'metric',
    'lang': 'ru'
}

while True:
    user_city = input('Введите город: ')
    if user_city == 'stop':
        break
    params['q'] = user_city
    data = requests.get('https://api.openweathermap.org/data/2.5/weather?', params=params).json()

    # pprint(data)
    temp = data['main']['temp']
    wind = data['wind']['speed']
    cursor.execute('''
    INSERT INTO weather (city,temp,wind) VALUES(?,?,?);
    ''', (user_city.title(), temp, wind))
    weather.commit()
    print(user_city, temp, wind)

weather.close()
