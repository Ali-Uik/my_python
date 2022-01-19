from configs import *
from telebot import TeleBot
from googletrans import Translator
from keyboards import *

translator = Translator(service_urls=['translate.google.com'])
word = 'привет'
print(word)
english_word = translator.translate(text=word, dest='en').text
print(english_word)
