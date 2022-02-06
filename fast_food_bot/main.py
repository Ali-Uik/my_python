from aiogram import Bot, Dispatcher, executor
# Bot - объект бота, Dispatcher - слушатель действий бота, executor - запускатель бота
from aiogram.types import Message, CallbackQuery
# Типы данных, которые приходят боту
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')
bot = Bot(token)
dp = Dispatcher(bot)  # Создали объект слежки ботам


@dp.message_handler(commands=['start'])
async def start(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, 'Это тестовый бот доставки еды')
