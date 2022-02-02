from configs import *
from telebot import TeleBot

bot = TeleBot(TOKEN, parse_mode='HTML')


@bot.message_handler(commands=['start', 'help'])
def print_message(message):
    chat_id = message.chat.id
    if message.text == '/start':
        bot.send_message(chat_id, 'Assalomu aleykum foydalanuvchi. Bu bot yordamida siz qazo namozlaringizning '
                                  'xisob-kitobini yuritishingiz mumkin')
    else:
        print('ERROR')


bot.polling(none_stop=True)
