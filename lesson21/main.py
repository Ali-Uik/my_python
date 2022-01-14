from configs import *
from telebot import TeleBot
from googletrans import Translator
from keyboards import *

bot = TeleBot(TOKEN, parse_mode='HTML')


@bot.message_handler(commands=['start', 'help', 'history'])
def command_start(message):
    chat_id = message.chat.id
    if message.text == '/start':
        bot.send_message(chat_id, f'''Привет <b>{message.from_user.first_name}</b>
    Я бот перевода и определения слов и текста''', reply_markup=generate_phone_number())
        cursor.execute('''SELECT * FROM users WHERE telegram_id = ? ''', (chat_id,))
        user = cursor.fetchone()
        if user:
            bot.send_message(chat_id, 'Что желаета сделат?')
        else:
            pass
        # TODO сделать функцию регистрации
    elif message.text == '/help':
        bot.send_message(chat_id,
                         f'''Данный бот был создан при поддержке <b>PROWEB</b>.При создании бота ни один студент не пострадал. Если у вас есть вопросы или что-то сломалось пишите сюда: @aliuiktraslatorbot''')
    elif message.text == '/history':
        bot.send_message(chat_id, 'Ваша история:')


bot.polling(none_stop=True)
