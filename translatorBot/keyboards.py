from telebot.types import ReplyKeyboardMarkup, KeyboardButton


# ReplyKeyboardMarkup - кнопкаларни ташийдиган контейнер.

def generate_phone_number():  # фойдаланувчининг тел номерини олади
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton(text='Отправьте свой контакт!', request_contact=True)
    # request_contact=True - шу команда тел номерни жунатади
    markup.add(btn)
    return markup


def choose_command():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    translate = KeyboardButton(text='Перевод \U0001F504')
    definition = KeyboardButton(text='Определение \U0001F4DD')
    markup.add(translate, definition)
    return markup
