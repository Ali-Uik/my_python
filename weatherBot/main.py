from aiogram import Bot, Dispatcher, executor, types
import requests

# Bot - объект бота, Dispatcher - слушатель действий бота, executor - запускатель бота
from aiogram.types import Message, CallbackQuery, Location, ReplyKeyboardMarkup
# Типы данных, которые приходят боту
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')
bot = Bot(token)
dp = Dispatcher(bot)  # Создали объект слежки ботам


@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    current_lat = message.location.latitude
    current_lon = message.location.longitude
    location_name1 = location_name(current_lat, current_lon)
    print(location_name1)
    data = weather(location_name1)
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    country = data['sys']['country']
    reply = "Cтрана: {}\nМесто: {}\nТемпература:  {} °C\nВетер: {} км/ч\nВлажность: {} %\nДавление: {} мм рт. ст." \
        .format(country, location_name1, temp, wind, humidity, pressure)
    await message.answer(reply)


def location_name(current_lat, current_lon):
    params = {
        'lat': current_lat,
        'lon': current_lon,
        'limit': 4,
        'appid': 'd0c4c1e4babd454e692db213ba832310',  # myAPI keys in openweathermap.org
    }
    data = requests.get('https://api.openweathermap.org/data/2.5/weather?', params=params).json()
    location_name = data['name']
    return location_name


def weather(location_name):
    params = {
        'appid': 'd0c4c1e4babd454e692db213ba832310',  # myAPI keys in openweathermap.org
        'units': 'metric',
        'lang': 'ru'
    }
    params['q'] = location_name
    data = requests.get('https://api.openweathermap.org/data/2.5/weather?', params=params).json()
    return data


executor.start_polling(dp, skip_updates=True)
