from aiogram import Bot, Dispatcher, executor
# Bot - объект бота, Dispatcher - слушатель действий бота, executor - запускатель бота
from aiogram.types import Message, CallbackQuery
# Типы данных, которые приходят боту
import os
from dotenv import load_dotenv
import sqlite3
from keyboards import *

load_dotenv()
token = os.getenv('TOKEN')
bot = Bot(token)
dp = Dispatcher(bot)  # Создали объект слежки ботам


@dp.message_handler(commands=['start'])
async def start(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, 'Это тестовый бот доставки еды')
    await register_user(message)
    await show_main_menu(message)


async def register_user(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    database = sqlite3.connect('fastfood.db')
    cursor = database.cursor()
    try:
        cursor.execute('''INSERT INTO users(full_name,telegram_id) VALUES (?,?)''', (full_name, chat_id))
        database.commit()
        await bot.send_message(chat_id, 'Регистрация прошло успешно!')
    except:
        await bot.send_message(chat_id, 'Авторизация прошло успешно!')
    database.close()
    await create_cart(message)


# TODO: Прописать функцию создания корзины пользователья
async def create_cart(message: Message):
    chat_id = message.chat.id
    database = sqlite3.connect('fastfood.db')
    cursor = database.cursor()
    try:
        cursor.execute('''INSERT INTO carts(user_id) VALUES 
        (
        (SELECT user_id FROM users WHERE telegram_id = ?;)
        )''', (chat_id,))
        database.commit()
    except:
        pass
    database.close()


async def show_main_menu(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, 'Выберите направление: ', reply_markup=generate_main_menu())


@dp.message_handler(lambda message: '✔ Сделать заказ' in message.text)
async def make_order(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, 'Выберите категорию: ', reply_markup=generate_category_menu())


executor.start_polling(dp, skip_updates=True)
