import os
import sqlite3
from telebot import TeleBot
from keyboards import *
import random
import re
import requests
from utils import *

db = sqlite3.connect('wallpapers.db', check_same_thread=False)
cursor = db.cursor()
TOKEN = '5135401313:AAHKApQ6bLczyMsCrL62suNQEmf8DGgfGsI'  # t.me/desktop_mockup_bot
bot = TeleBot(TOKEN, parse_mode='HTML')


@bot.message_handler(commands=['start'])
def command_start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Привет здесь ты найдеш обои на любой вкус!')
    shou_categories(message)


def shou_categories(message):
    chat_id = message.chat.id
    cursor.execute('''SELECT category_name FROM categories;''')
    categories = cursor.fetchall()
    msg = bot.send_message(chat_id, 'Выберите категорию', reply_markup=generate_categories(categories))
    bot.register_next_step_handler(msg, get_image)


def get_image(message):
    chat_id = message.chat.id
    category = message.text
    cursor.execute('''SELECT category_id FROM categories WHERE category_name = ?;''', (category,))
    category_id = cursor.fetchone()[0]
    cursor.execute('''SELECT image_link FROM images WHERE category_id = ?;''', (category_id,))
    image_links = cursor.fetchall()
    random_index = random.randint(0, len(image_links) - 1)
    random_image_link = image_links[random_index][0]
    resolution = re.search(r'[0-9]+x[0-9]+', random_image_link)[0]
    cursor.execute('''SELECT image_id FROM images WHERE image_link = ?;''', (random_image_link,))

    responseImage = requests.get(random_image_link).content
    image_name = random_image_link.replace('https://images.wallpaperscraft.ru/image/single/', '')
    with open(file=f'{image_name}', mode='wb') as file:
        file.write(responseImage)
    crop_image_to_mobile(image_name)
    watermark_text(image_name)
    # os.remove(image_name)  # Удалит скаченную картину
    image_id = cursor.fetchone()[0]
    db.commit()

    img = open(f'water_{image_name}', mode='rb')
    try:
        bot.send_photo(chat_id=chat_id,
                       photo=img,
                       caption=f'Разрешение {resolution}',
                       reply_markup=download_button(image_id))
        img.close()
        os.remove(image_name)
        os.remove(f'water_{image_name}')
        os.remove(f'crop_{image_name}')
    except Exception as e:
        new_image_link = random_image_link.replace(resolution, '1920x1080')
        bot.send_photo(chat_id=chat_id,
                       photo=new_image_link,
                       caption=f'Разрешение 1920x1080 заменили',
                       reply_markup=download_button(image_id))
    shou_categories(message)


@bot.callback_query_handler(func=lambda call: 'downloadd' in call.data)
def downloadd_reaction(call):
    _, image_id = call.data.split('_')
    print(image_id)
    cursor.execute('''SELECT image_link FROM images WHERE image_id = ?;''', (image_id,))
    image_link = cursor.fetchone()[0]
    print(image_link)
    bot.send_document(chat_id=call.message.chat.id, data=image_link, document=image_link)
    bot.answer_callback_query(call.id, show_alert=False)


@bot.callback_query_handler(func=lambda call: 'downloadm' in call.data)
def downloadm_reaction(call):
    _, image_id = call.data.split('_')
    print(image_id)
    cursor.execute('''SELECT image_link FROM images WHERE image_id = ?;''', (image_id,))
    image_link = cursor.fetchone()[0]
    responseImage = requests.get(image_link).content
    image_name = image_link.replace('https://images.wallpaperscraft.ru/image/single/', '')
    with open(file=f'{image_name}', mode='wb') as file:
        file.write(responseImage)
    crop_image_to_mobile(image_name)
    img = open(f'crop_{image_name}', mode='rb')
    print(image_link)
    bot.send_document(chat_id=call.message.chat.id, data=img, document=img)
    img.close()
    os.remove(image_name)
    os.remove(f'crop_{image_name}')
    bot.answer_callback_query(call.id, show_alert=False)


bot.polling(none_stop=True)
