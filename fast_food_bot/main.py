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
bot = Bot(token, parse_mode='HTML')
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


@dp.callback_query_handler(lambda call: 'category' in call.data)
async def show_products(call: CallbackQuery):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    _, category_id = call.data.split('_')  # _ Это штука нам не нужна
    category_id = int(category_id)
    await bot.edit_message_text('Выберите продукт: ', chat_id, message_id,
                                reply_markup=generate_products_menu(category_id))


@dp.callback_query_handler(lambda call: 'product' in call.data)
async def show_detail_products(call: CallbackQuery):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    # product_1 -> _='product' product_id=1
    _, product_id = call.data.split('_')
    database = sqlite3.connect('fastfood.db')
    cursor = database.cursor()
    # Полужаем всю информацию из бази о продукте
    cursor.execute('''SELECT product_id,product_name, price, ingredients, category_id, images 
    FROM products
    WHERE product_id = ?;''', (product_id,))
    product = cursor.fetchone()
    print(product)
    database.close()
    await bot.delete_message(chat_id, message_id)
    with open(product[5], mode='rb') as img:
        await bot.send_photo(chat_id,
                             photo=img,
                             caption=f"""<strong>{product[1]}</strong>\n<strong>Ингридиенты: {product[3]}</strong>\n<strong>Цена: {product[2]}</strong>""",
                             reply_markup=generate_product_detail_menu(
                                 product_id=product_id,
                                 category_id=product[4]))


@dp.callback_query_handler(lambda call: call.data.startswith("cart"))
async def add_product_cart(call: CallbackQuery):
    # cart_1_2 - 1 - id product, 2 - quantiry
    chat_id = call.message.chat.id
    _, product_id, quantity = call.data.split('_')
    product_id, quantity = int(product_id), int(quantity)
    database = sqlite3.connect('fastfood.db')
    cursor = database.cursor()
    # получаем корзину пользователья
    cursor.execute('''
    SELECT cart_id FROM carts
    WHERE user_id = (SELECT user_id FROM users WHERE telegram_id = ?);
    ''', (chat_id,))
    cart_id = cursor.fetchone()[0]
    # Получаем информацию о продукте  название и цена
    cursor.execute('''SELECT product_name, price FROM products WHERE product_id = ?''', (product_id,))
    product_name, price = cursor.fetchone()  # ('Лаваш', 25000)
    final_price = quantity * price  # Общая цена
    try:
        cursor.execute('''
        INSERT INTO cart_products(cart_id, product_name, quantity, final_price)
        VALUES (?,?,?,?)''', (cart_id, product_name, quantity, final_price))
        database.commit()
        await bot.answer_callback_query(call.id, text='Продукт успешно добавлен')
    except:
        cursor.execute('''
        UPDATE cart_products
        SET quantity = ?,
        final_price = ?
        WHERE product_name = ? AND cart_id =?
        ''', (quantity, final_price, product_name, cart_id))
        database.commit()
        await bot.answer_callback_query(call.id, text='Количество успешно изменено')
    finally:
        database.close()


executor.start_polling(dp, skip_updates=True)
