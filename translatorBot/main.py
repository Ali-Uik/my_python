from configs import *
from telebot import TeleBot
from googletrans import Translator

bot = TeleBot(TOKEN)  # ботни регистрация килдик


@bot.message_handler(commands=['start', 'help', 'history'])   # start, help, history командаларига жавобан ишлайди
def command_start(message):  # message бу - бот кабул килиши керак булган хабар, яъни фойдаланувчи жунатадиган хабар
    print(message)


bot.polling(none_stop=True)  # ботнинг тухтамасдан ишлаши учун
