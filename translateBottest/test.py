from configs import *
from telebot import TeleBot
# from googletrans import Translator
from translate import Translator
from keyboards import *

translator = Translator(to_lang='en')
english_word = translator.translate('')
print(english_word)
