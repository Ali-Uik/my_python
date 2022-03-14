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


@bot.message_handler(regexp=r'Ro\'yxatdan o\'tish')
def sign_in(message):
    chat_id = message.chat.id
    word = bot.send_message(chat_id, 'Ismingizni kiriting!')
    bot.register_next_step_handler(word, sign_up_start)


def sign_in_start(message):
    chat_id = message.chat.id
    user_text = message.text
    print(f'user_text={user_text}')
    print(type(user_text))
    if type(user_text) is int:
        cursor.execute('''SELECT db_id FROM users WHERE db_id = ?;''', (user_text,))
        db_id = cursor.fetchall()
        print(db_id)
        db.close()
        if db_id:
            bot.send_message(chat_id, 'Ishladi')
        else:
            bot.send_message(chat_id,
                             'Siz kiritgan ID bizning bazada mavjud emas. Iltimos ro\'yxatdan o\'tish tugmasini bosib, ro\'yxatdan o\'ting.')
    else:
        bot.send_message(chat_id, 'Siz noto\'g\'ri ma\'lumot kiritdingiz!')


def sign_up_start(message):
    chat_id = message.chat.id
    user_text = message.text
    print(user_text)
    cursor.execute('''SELECT MAX(id) FROM users;''')
    max_id = cursor.fetchone()[0]

    # db.commit()
    # bot.send_message(chat_id, max_id)
    # db.close()
    db_id = f'{chat_id}{max_id + 1}'
    cursor.execute('''INSERT INTO users(chat_id,db_id,user_name) VALUES (?,?,?);''',
                   (chat_id, db_id, user_text))
    db.commit()
    db.close()
    bot.send_message(chat_id,
                     f'Hurmatli <b>{user_text}</b> siz bizning botda ro\'yhatdan o\'tdingiz. Sizning botdagi IDingiz '
                     f'<b>{db_id}</b>.Siz bu ID orqali xoxlagan qurilmadan telegram orqali kirishingiz mumkin.')

    # def print_message(message):
    #     text = message.text
    #     print(text)


bot.polling(none_stop=True)
