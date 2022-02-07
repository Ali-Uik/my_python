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
