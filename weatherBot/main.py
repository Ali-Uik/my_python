from aiogram import Bot, Dispatcher, executor, types
from countryinfo import CountryInfo
# Bot - объект бота, Dispatcher - слушатель действий бота, executor - запускатель бота
from aiogram.types import Message, CallbackQuery, Location, ReplyKeyboardMarkup
# Типы данных, которые приходят боту
import os
from dotenv import load_dotenv

# import sqlite3
# from keyboards import *

load_dotenv()
token = os.getenv('TOKEN')
bot = Bot(token)
dp = Dispatcher(bot)  # Создали объект слежки ботам


@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    print(type(message))
    lat = message.location.latitude
    lon = message.location.longitude
    print(message)
    print(lat, lon)
    reply = "latitude:  {}\nlongitude: {}".format(lat, lon)
    await message.answer(reply)


executor.start_polling(dp, skip_updates=True)
