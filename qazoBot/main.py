from configs import *
from telebot import TeleBot
from keyboards import *

bot = TeleBot(TOKEN, parse_mode='HTML')


@bot.message_handler(commands=['start', 'help'])
def start(message):
    chat_id = message.chat.id
    if message.text == '/start':
        bot.send_message(chat_id, f'Assalomu aleykum foydalanuvchi. Bu botdan foydalanishingiz uchun oldin '
                                  'ro\'yxatdan o\'tishingiz kerak. Agar ro\'yxatdan o\'tgan bo\'lsangiz kirish '
                                  'tugmasini bosing ', reply_markup=sign_in_or_sign_up())
    else:
        print('ERROR')


@bot.message_handler(regexp=r'Kirish')
def sign_in(message):
    chat_id = message.chat.id
    word = bot.send_message(chat_id, 'Sizga bot tomandan berilgan IDni kiriting!')
    bot.register_next_step_handler(word, sign_in_start)


def sign_in_start(message):
    chat_id = message.chat.id
    user_text = message.text
    print(user_text)
    cursor.execute('''SELECT db_id FROM users;''')
    db_ids = cursor.fetchall()
    print(db_ids)
    for db_id in db_ids:
        print(db_id)
        if db_id == user_text:
            bot.send_message(chat_id, 'Ishladi')
        else:
            bot.send_message(chat_id, 'Ishlamadi')


# def print_message(message):
#     text = message.text
#     print(text)


bot.polling(none_stop=True)
