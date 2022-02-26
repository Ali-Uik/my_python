import sqlite3

from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from utils import build_inline_menu


def generate_main_menu():
    return ReplyKeyboardMarkup([
        [KeyboardButton(text='✔ Сделать заказ')],
        [KeyboardButton(text='📋 История заказов'), KeyboardButton(text='🛒 Корзина')]
    ], resize_keyboard=True)


def generate_category_menu():
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(text='Все меню', url='https://telegra.ph/Menyu-02-07-5')
    )
    database = sqlite3.connect('fastfood.db')
    cursor = database.cursor()
    cursor.execute('''SELECT category_id, category_name FROM categories;''')
    categories = cursor.fetchall()
    database.close()
    build_inline_menu(markup, categories, 'category')
    return markup


def generate_products_menu(category_id: int):
    markup = InlineKeyboardMarkup()
    database = sqlite3.connect('fastfood.db')
    cursor = database.cursor()
    cursor.execute('''SELECT product_id, product_name FROM products WHERE category_id = ?''',
                   (category_id,))
    products = cursor.fetchall()
    database.close()
    build_inline_menu(markup, products, 'product')
    return markup


def generate_product_detail_menu(product_id: int, category_id: int):
    # cart_1_2 -> cart - ключевое слово, 1 - id продукта, 2-количество продуктов
    markup = InlineKeyboardMarkup()
    number_list = [i for i in range(1, 10)]
    in_row = 3  # Сбрасиваем
    rows = len(number_list) // in_row
    if len(number_list) % in_row != 0:
        rows += 1
    start = 0
    end = in_row
    for i in range(rows):
        new_list = []
        for number in number_list[start:end]:
            new_list.append(InlineKeyboardButton(text=str(number), callback_data=f'cart_{product_id}_{number}'))
        markup.row(*new_list)
        start = end
        end += in_row
    markup.row(
        InlineKeyboardButton(text='Назад', callback_data=f'back_{category_id}')
    )
    return markup


def generate_cart_menu(cart_id: int):
    markup = InlineKeyboardMarkup
    markup.row(
        InlineKeyboardButton(text='🚀 Оформить заказ', callback_data=f'order_{cart_id}')
    )
    database = sqlite3.connect('fastfood.db')
    cursor = database.cursor()
    cursor.execute('''SELECT cart_product_id, product_name 
    FROM cart_products
    WHERE cart_id=?''', (cart_id,))
    cart_products = cursor.fetchall()
    database.close()
    for product_id, product_name in cart_products:
        markup.row(
            InlineKeyboardButton(text=f'❌ {product_name}', callback_data=f'' )
        )
