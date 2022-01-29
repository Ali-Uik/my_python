import sqlite3
from telebot import TeleBot
from keyboards import *
import random
import re

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
    image_id = cursor.fetchone()[0]
    try:
        bot.send_photo(chat_id=chat_id,
                       photo=random_image_link,
                       caption=f'Разрешение {resolution}')
    except Exception as e:
        new_image_link = random_image_link.replace(resolution, '1920x1080')
        bot.send_photo(chat_id=chat_id,
                       photo=new_image_link,
                       caption=f'Разрешение 1920x1080 заменили')
    shou_categories(message)
    db.commit()


bot.polling(none_stop=True)
