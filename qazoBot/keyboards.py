from telebot.types import KeyboardButton, ReplyKeyboardMarkup


def sign_in_or_sign_up():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    sign_in = KeyboardButton(text='Kirish')
    sing_up = KeyboardButton(text='Ro\'yxatdan o\'tish')
    markup.add(sign_in, sing_up)
    return markup


def choose_command():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    bomdod = KeyboardButton(text='Bomdod')
    peshin = KeyboardButton(text='Peshin')
    asr = KeyboardButton(text='Asr')
    shom = KeyboardButton(text='Shom')
    xufton = KeyboardButton(text='Xufton')
    vitr = KeyboardButton(text='Vitr vojib')
    markup.add(bomdod, peshin, asr, shom, xufton, vitr)
    return markup
